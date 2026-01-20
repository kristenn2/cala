from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from .models import Experience

User = get_user_model()

from django.urls import reverse_lazy
class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ExperienceListView(ListView):
    model = Experience
    context_object_name = 'experiences'
    template_name = 'app/experience_list.html'
    success_url = reverse_lazy('experience')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if query:
            filtered_experiences = Experience.objects.filter(title__icontains=query).order_by('-created_at')
        else:
            filtered_experiences = Experience.objects.all().order_by('-created_at')
        context['experiences'] = filtered_experiences
        context['total_experiences'] = Experience.objects.count()
        context['total_users'] = User.objects.count()
        return context

class ExperienceDetailView(DetailView):
    model = Experience
    context_object_name = 'experience'
    template_name = 'app/experience_detail.html'

class ExperienceCreateView(CreateView):
    model = Experience
    fields = ['title', 'user', 'content', 'category']
    template_name = 'app/experience_create.html'
    success_url = reverse_lazy('experience')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

class ExperienceUpdateView(UpdateView):
    model = Experience
    fields = ['title', 'user', 'content', 'category']
    template_name = 'app/experience_update.html'
    success_url = reverse_lazy('experience')

class ExperienceDeleteView(DeleteView):
    model = Experience
    context_object_name = 'experience'
    template_name = 'app/experience_delete.html'
    success_url = reverse_lazy('experience')