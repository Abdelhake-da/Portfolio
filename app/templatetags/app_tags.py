from django import template
from core.models import *

register = template.Library()

@register.filter
def get_category_items(categories):
    skills = []
    for category in categories:
        skill = Skill.objects.filter(category=category, is_visible=True)
        if len(skill) > 0:
            skills.append([category, skill])
    return skills
@register.filter
def get_project(project_id):
    try:
        return Project.objects.get(id=project_id)
    except Exception as e:
        return None

@register.filter
def clean_tech_list(value):
    if not value:
        return ""
    return ", ".join(t.strip() for t in value.split(",") if t.strip())