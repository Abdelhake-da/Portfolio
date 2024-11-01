from django.contrib import admin
from django.apps import apps

# Get all models for the current app
app_models = apps.get_app_config('core').get_models()

# Register each model in the admin
for model in app_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        # If model is already registered, skip it
        pass
