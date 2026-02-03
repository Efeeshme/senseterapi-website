from django.shortcuts import render
from .models import Branch, TeamMember, Service

def home(request):
    branches = Branch.objects.filter(is_active=True)
    team = TeamMember.objects.filter(is_active=True).select_related("branch")
    services = Service.objects.filter(is_active=True)
    return render(
        request,
        "web/home.html",
        {"branches": branches, "team": team, "services": services},
    )