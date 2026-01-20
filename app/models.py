from django.db import models
from django.conf import settings


class Experience(models.Model):
    CATEGORY_CHOICES = [
        ('travel_log', 'Travel Log'),
        ('food_share', 'Food Sharing'),
        ('cultural_story', 'Cultural Story'),
        ('others', 'Others'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class VirtualTour(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LanguagePartner(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    target_language = models.CharField(max_length=100)
    proficiency_level = models.CharField(max_length=50)
    availability = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.target_language}"


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    rating = models.IntegerField(default=5)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username}"


class ResourceMaterial(models.Model):
    RESOURCE_TYPES = [
        ('guide', 'Guide'),
        ('article', 'Article'),
        ('educational', 'Educational Material')
    ]

    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    resource_type = models.CharField(max_length=50, choices=RESOURCE_TYPES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title