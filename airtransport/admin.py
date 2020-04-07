from django.contrib import admin
from django.apps import apps
from django.contrib.auth.models import Group, User

models = apps.get_models()

admin.site.unregister(Group)
admin.site.unregister(User)
for model in models:
    admin.site.register(model)
