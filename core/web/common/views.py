from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from models.project.models import Project


@login_required(login_url="/user/login/")
def index(request):
    projects = Project.objects.all()
    return render(request, "index.html", {"projects": projects})
