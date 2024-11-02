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
    if "proj" not in request.session:
        request.session["proj"] = None
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
    return render(request, 'pages/index.html',context)
def get_project(request):
    # Get action from GET parameters to either increment or decrement
    proj = request.GET.get("proj")
    project = Project.objects.get(id=proj)

    return render(request, "components/project_description.html", {"project": project})

from django.http import JsonResponse

def counter_view(request):
    # Initialize counter if it doesn't exist in the session
    if "counter" not in request.session:
        request.session["counter"] = 0

    # Get action from GET parameters to either increment or decrement
    action = request.GET.get("action")
    if action == "increment":
        request.session["counter"] += 1
    elif action == "decrement":
        request.session["counter"] -= 1

    # Save the updated session
    request.session.modified = True

    # Return only the counter value as HTML for HTMX
    return HttpResponse(request.session["counter"])

def counter_page(request):
    return render(request, "htmx_test.html")



def comment_page(request):
    # Initialize comments list in session if it doesn't exist
    if "comments" not in request.session:
        request.session["comments"] = []

    return render(request, "comment_page.html")

def add_comment(request):
    # Retrieve comment text from the request
    comment_text = request.POST.get("comment")
    if comment_text:
        # Append the new comment to the session's comments list
        comments = request.session.get("comments", [])
        comments.append(comment_text)
        request.session["comments"] = comments
        request.session.modified = True

    # Render the comments section HTML only
    return render(request, "comments_section.html", {"comments": request.session["comments"]})