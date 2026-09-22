from django.db.models.signals import pre_save
from django.dispatch import receiver

from . import models
from .services.image_optimizer import optimize_uploaded_field


@receiver(pre_save, sender=models.Project)
def optimize_project_image(sender, instance, **kwargs):
    optimize_uploaded_field(instance, "main_image")


@receiver(pre_save, sender=models.PersonalInfo)
def optimize_personal_info_images(sender, instance, **kwargs):
    optimize_uploaded_field(instance, "myimg")
    optimize_uploaded_field(instance, "background")
