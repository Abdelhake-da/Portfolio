import os
from django.db import models

def upload_to(instance, filename):
    # Get the file extension
    ext = filename.split('.')[-1]
    # Create a unique file name based on a UUID and current date
    new_filename = f"{instance.title}.{ext}"
    # Return the custom path
    return os.path.join('Projects', new_filename)
def my_img_upload_to(instance, filename):
    # Get the file extension
    ext = filename.split('.')[-1]
    # Create a unique file name based on a UUID and current date
    new_filename = f"myimg.{ext}"
    # Return the custom path
    return os.path.join('Base', new_filename)
def background_upload_to(instance, filename):
    # Get the file extension
    ext = filename.split('.')[-1]
    # Create a unique file name based on a UUID and current date
    new_filename = f"background.{ext}"
    # Return the custom path
    return os.path.join('Base', new_filename)
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=True,blank=True)
    main_image = models.ImageField(upload_to=upload_to)
    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    date = models.CharField(max_length=20,null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    date = models.CharField(max_length=20,null=True)
    description = models.TextField()

    def __str__(self):
        return self.degree
class OnlineCourse(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(null=True)
    certificate_url = models.URLField()
    def __str__(self) -> str:
        return self.title
class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=15)
    age = models.IntegerField()
    email = models.EmailField()
    web_site = models.URLField(null=True, blank=True)
    city = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    freelance = models.CharField(max_length=100,null=True)
    what_i_do = models.CharField(max_length=300,null=True)
    description_about_me = models.TextField(null=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    myimg = models.ImageField(upload_to=my_img_upload_to,null=True,blank=True)
    background = models.ImageField(upload_to=background_upload_to,null=True,blank=True)
    my_resume = models.FileField(upload_to='my_resume', blank=True, null=True)

    def __str__(self):
        return self.full_name
class SkillCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__(self):
        return self.name