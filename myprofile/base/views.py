from django.shortcuts import render, redirect
from .models import Survey,Projects

def index(request):
    projects = Projects.objects.all()
    return render(request, 'base/index.html', {'projects': projects})

def survey_view(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comments = request.POST.get('comments', '')

        survey = Survey(rating=rating, comments=comments)
        survey.save()

    
    return index(request)
