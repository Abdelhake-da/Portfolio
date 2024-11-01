from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def compress_image(image, max_width=1080, max_height=1080, quality=80):
    """
    Compresses an image without significant quality loss.

    Parameters:
        image: The original image file to compress.
        max_width: The maximum width to resize (maintains aspect ratio). Adjust as needed.
        max_height: The maximum height to resize (maintains aspect ratio). Adjust as needed.
        quality: Quality setting for compression (0-100). Lower values reduce file size but affect quality.

    Returns:
        Compressed image file ready for saving.
    """
    # Open the image file
    img = Image.open(image)
    print(f"{'*' * 20} {image.name} {'*' * 20}")

    # Convert to RGB if needed (JPEGs need to be in RGB mode)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    print(f"{'*' * 20} {image.name} {'*' * 20}")
    # Resize image if it’s wider than max_width or taller than max_height
    if img.width > max_width or img.height > max_height:
        aspect_ratio = img.width / img.height
        if aspect_ratio > 1:  # Wider than tall
            new_width = max_width
            new_height = int(max_width / aspect_ratio)
        else:  # Taller than wide
            new_height = max_height
            new_width = int(max_height * aspect_ratio)
        img = img.resize((new_width, new_height), Image.LANCZOS)

    # Save image to BytesIO object for compressed version
    img_io = BytesIO()
    img.save(img_io, format="JPEG", quality=quality)  # Lower quality for more compression
    compressed_image = ContentFile(img_io.getvalue(), name=image.name)

    return compressed_image
