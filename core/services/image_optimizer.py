import io
import logging
from pathlib import Path

from django.apps import apps
from django.core.files.base import ContentFile
from PIL import Image

logger = logging.getLogger(__name__)

DEFAULT_QUALITY = 80

# (model_label, field names) — the single source of truth for which
# image fields are converted to WebP, used by the signal, the admin
# view and the management command.
IMAGE_FIELDS = (
    ("core.Project", ("main_image",)),
    ("core.PersonalInfo", ("myimg", "background")),
)


def convert_to_webp(field_file, quality=DEFAULT_QUALITY):
    """Convert an ImageField file to WebP.

    Returns (new_name, ContentFile) or None when the field is empty,
    already WebP, or unreadable.
    """
    if not field_file or field_file.name.lower().endswith(".webp"):
        return None
    try:
        field_file.open("rb")
        img = Image.open(field_file)
        img.load()
    except Exception as exc:
        logger.warning("Cannot read image %s: %s", field_file.name, exc)
        return None
    if img.mode in ("P", "LA"):
        img = img.convert("RGBA")
    elif img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGB")
    buffer = io.BytesIO()
    img.save(buffer, "WEBP", quality=quality)
    new_name = str(Path(field_file.name).with_suffix(".webp"))
    return new_name, ContentFile(buffer.getvalue(), name=Path(new_name).name)


def optimize_uploaded_field(instance, field_name, quality=DEFAULT_QUALITY):
    """Swap a model's image field for a WebP version before it is saved.

    The original uploaded file is never written to storage.
    """
    result = convert_to_webp(getattr(instance, field_name), quality)
    if result is None:
        return False
    _new_name, content = result
    setattr(instance, field_name, content)
    return True


def iter_image_fields():
    """Yield (obj, field_name) for every image field in IMAGE_FIELDS."""
    for model_label, field_names in IMAGE_FIELDS:
        model = apps.get_model(model_label)
        for obj in model.objects.all():
            for name in field_names:
                yield obj, name


def pending_images():
    """Return [(obj, field_name, file_name)] for stored non-WebP images."""
    pending = []
    for obj, name in iter_image_fields():
        field = getattr(obj, name)
        if field and not field.name.lower().endswith(".webp"):
            pending.append((obj, name, field.name))
    return pending


def optimize_field(obj, field_name, quality=DEFAULT_QUALITY):
    """Convert one stored field to WebP (writes the file, does not save obj).

    Returns (report_line, changed).
    """
    field = getattr(obj, field_name)
    if not field or field.name.lower().endswith(".webp"):
        return None, False
    old_name = field.name
    try:
        old_size = field.storage.size(old_name)
    except OSError:
        old_size = 0
    result = convert_to_webp(field, quality)
    if result is None:
        return f"FAILED: {old_name}", False
    new_name, content = result
    field.save(new_name, content, save=False)
    return (
        f"{old_name} -> {new_name} "
        f"({old_size / 1024:.0f} KB -> {content.size / 1024:.0f} KB)",
        True,
    )


def optimize_all_images(quality=DEFAULT_QUALITY):
    """Convert every stored non-WebP image. Returns report lines."""
    reports = []
    for model_label, field_names in IMAGE_FIELDS:
        model = apps.get_model(model_label)
        for obj in model.objects.all():
            updated = []
            for name in field_names:
                report, changed = optimize_field(obj, name, quality)
                if report:
                    reports.append(report)
                if changed:
                    updated.append(name)
            if updated:
                obj.save(update_fields=updated)
    return reports
