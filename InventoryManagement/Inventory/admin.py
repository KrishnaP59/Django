from django.contrib import admin
from .models import *


@admin.register(smartphone,laptop)
class ViewAdmin(admin.ModelAdmin):
    pass
