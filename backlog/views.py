from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from .models import Teams, Maps
from django.contrib.auth.decorators import login_required
#from .forms import TaskEditForm, TaskEditModelForm
from rest_framework import generics
#from .serializers import TaskSerializer, TaskClassSerializer
from rest_framework.permissions import IsAuthenticated
    # Create your views here.
     

@login_required
def home (request):
#    if request.user.is_superuser or request.user.is_staff:
        return redirect('teams')
#    else:
#        return redirect('maps')
    

@login_required
def teams(request):
    teams = Teams.object.all()
    return render(request, 'backlog/teams.html', {'teams': teams})


@login_required
def maps(request, team_id):
    maps = get_object_or_404(Maps, id=team_id)
    maps = Maps.object.all()
    return render(request, "backlog/maps.html",)
