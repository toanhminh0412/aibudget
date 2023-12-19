from django.apps import apps
from django.contrib import admin

# Register all models
[admin.site.register(model) for model in apps.get_app_config('budgetmanager').get_models()]