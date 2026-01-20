from django.contrib import admin
from .models import Experience, VirtualTour, LanguagePartner, Feedback, ResourceMaterial


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'created_at')


@admin.register(VirtualTour)
class VirtualTourAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'created_by', 'created_at')


@admin.register(LanguagePartner)
class LanguagePartnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'target_language', 'proficiency_level', 'availability')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'submitted_at')


@admin.register(ResourceMaterial)
class ResourceMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'uploaded_by', 'uploaded_at')
