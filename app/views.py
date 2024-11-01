from django.shortcuts import render
from core.models import *
import os
from django.http import HttpResponse, Http404
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test

# Check if the user is a superuser
def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def download_database(request):
    # Path to the sqlite database file
    db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')

    # Check if the file exists
    if not os.path.exists(db_path):
        raise Http404("Database file not found.")

    # Open the file and prepare it for download
    with open(db_path, 'rb') as db_file:
        response = HttpResponse(db_file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="db.sqlite3"'
        return response

def index(request):
    # Render the index page with the current counter value
    personal_info = PersonalInfo.objects.first()
    category = SkillCategory.objects.all()
    resume = [Education.objects.all(), OnlineCourse.objects.all(), Experience.objects.all()]
    projects = Project.objects.all()
    context={
        'pi' : personal_info,
        'category' : category,
        'resume' : resume,
        'projects' : projects

    }
    return render(request, 'index.html',context)
