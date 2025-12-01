from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request, 'skills.html')



from .models import Experience

def experience(request):
    experiences = Experience.objects.all().order_by('-date')  # most recent first
    return render(request, 'experience.html', {'experiences': experiences})
def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render, get_object_or_404
from .models import Project

def projects(request):
    all_projects = Project.objects.order_by('-created_at')
    return render(request, 'projects.html', {'projects': all_projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})