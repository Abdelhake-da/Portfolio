from django import template
from core.models import *

register = template.Library()

@register.filter
def get_category_items(categories):
    skills = []
    for category in categories:
        skill = Skill.objects.filter(category=category)
        if len(skill) > 0:
            skills.append([category, skill])
    return skills
