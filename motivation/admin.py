# from django.contrib import admin
# from . import models
# # Register your models here.
# admin.site.register(models.Actor)
# admin.site.register(models.Quote)
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  # Step 1: Import the necessary class
from .models import Actor, Quote  # Import your models

# Step 2: Register models using ImportExportModelAdmin
@admin.register(Actor)
class ActorAdmin(ImportExportModelAdmin):
    pass

@admin.register(Quote)
class QuoteAdmin(ImportExportModelAdmin):
    pass

