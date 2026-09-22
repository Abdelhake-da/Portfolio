from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .services.image_optimizer import optimize_all_images, pending_images


@require_http_methods(["GET", "POST"])
def optimize_images_view(request):
    """Admin page listing uncompressed images and converting them on POST."""
    if request.method == "POST":
        reports = optimize_all_images()
        for line in reports:
            messages.info(request, line)
        if reports:
            messages.success(request, f"تم تحويل {len(reports)} صورة إلى WebP.")
        else:
            messages.info(request, "كل الصور مضغوطة بالفعل.")
        return redirect("optimize_images")
    return render(
        request,
        "admin/optimize_images.html",
        {"title": "ضغط الصور", "pending": pending_images()},
    )
