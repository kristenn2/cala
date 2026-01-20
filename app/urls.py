from django.urls import path
from .views import HomePageView, AboutPageView, ExperienceListView, ExperienceDetailView, ExperienceCreateView, ExperienceUpdateView, ExperienceDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('experience/', ExperienceListView.as_view(), name='experience'),
    path('experience/<int:pk>', ExperienceDetailView.as_view(), name='experience_detail'),
    path('experience/create', ExperienceCreateView.as_view(), name='experience_create'),
    path('experience/<int:pk>/edit', ExperienceUpdateView.as_view(), name='experience_update'),
    path('experience/<int:pk>/delete', ExperienceDeleteView.as_view(), name='experience_delete'),
]