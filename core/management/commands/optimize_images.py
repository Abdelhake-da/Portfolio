import io
from pathlib import Path

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from PIL import Image

from core.models import PersonalInfo, Project


class Command(BaseCommand):
    help = (
        "Convert uploaded images (project main images, profile and background "
        "images) to WebP and update the model fields. Old files are kept."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--quality",
            type=int,
            default=80,
            help="WebP quality (1-100, default: 80)",
        )

    def convert_field(self, obj, field_name, quality):
        field = getattr(obj, field_name)
        if not field:
            return None
        if field.name.lower().endswith(".webp"):
            self.stdout.write(f"  skip (already WebP): {field.name}")
            return None
        try:
            img = Image.open(field.path)
        except (FileNotFoundError, ValueError) as exc:
            self.stderr.write(f"  missing/unreadable file {field.name}: {exc}")
            return None
        if img.mode == "P":
            img = img.convert("RGBA")
        elif img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGB")
        buffer = io.BytesIO()
        img.save(buffer, "WEBP", quality=quality)
        old_name = field.name
        new_name = str(Path(old_name).with_suffix(".webp"))
        field.save(new_name, ContentFile(buffer.getvalue()), save=False)
        old_size = field.storage.size(old_name)
        new_size = buffer.tell()
        self.stdout.write(
            f"  {old_name} -> {new_name} "
            f"({old_size / 1024:.0f} KB -> {new_size / 1024:.0f} KB)"
        )
        return True

    def handle(self, *args, **options):
        quality = options["quality"]
        changed = 0

        for project in Project.objects.all():
            if self.convert_field(project, "main_image", quality):
                project.save(update_fields=["main_image"])
                changed += 1

        for pi in PersonalInfo.objects.all():
            updated = [
                name
                for name in ("myimg", "background")
                if self.convert_field(pi, name, quality)
            ]
            if updated:
                pi.save(update_fields=updated)
                changed += len(updated)

        self.stdout.write(self.style.SUCCESS(f"Done. {changed} image(s) converted."))
