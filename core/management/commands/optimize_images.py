from django.core.management.base import BaseCommand

from core.services.image_optimizer import optimize_all_images


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

    def handle(self, *args, **options):
        reports = optimize_all_images(quality=options["quality"])
        for line in reports:
            self.stdout.write(f"  {line}")
        self.stdout.write(
            self.style.SUCCESS(f"Done. {len(reports)} image(s) converted.")
        )
