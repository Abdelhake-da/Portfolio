from django.contrib import admin
from django.apps import apps
from .models import (
    Project, Experience, Education, OnlineCourse,
    SkillCategory, Skill, PersonalInfo,
)


class VisibilityAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_visible')
    list_editable = ('is_visible',)


class PersonalInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'full_name', 'birth_date', 'phone_number', 'age', 'email',
                'web_site', 'city', 'degree', 'freelance', 'what_i_do',
                'description_about_me', 'facebook', 'twitter', 'linkedin',
                'github', 'instagram', 'myimg', 'background', 'my_resume',
            ),
        }),
        ('Visibility', {
            'classes': ('collapse',),
            'fields': (
                'show_full_name', 'show_birth_date', 'show_phone_number',
                'show_age', 'show_email', 'show_web_site', 'show_city',
                'show_degree', 'show_freelance', 'show_what_i_do',
                'show_description_about_me', 'show_facebook', 'show_twitter',
                'show_linkedin', 'show_github', 'show_instagram',
                'show_myimg', 'show_background', 'show_my_resume',
            ),
        }),
    )


admin.site.register(Project, VisibilityAdmin)
admin.site.register(Experience, VisibilityAdmin)
admin.site.register(Education, VisibilityAdmin)
admin.site.register(OnlineCourse, VisibilityAdmin)
admin.site.register(SkillCategory, VisibilityAdmin)
admin.site.register(Skill, VisibilityAdmin)
admin.site.register(PersonalInfo, PersonalInfoAdmin)

# Register each remaining model in the admin
app_models = apps.get_app_config('core').get_models()

for model in app_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        # If model is already registered, skip it
        pass
