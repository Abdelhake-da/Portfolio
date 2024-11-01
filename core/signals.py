from django.db.models.signals import pre_save
from django.dispatch import receiver
from .utils import compress_image
from . import models

@receiver(pre_save, sender=models.Project)
def compress_image_on_save(sender, instance, **kwargs):
    if instance.main_image:
        instance.image = compress_image(instance.main_image)
