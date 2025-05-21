from django.urls import path
from .views import home, teams, maps
 
urlpatterns = [
    path('', home, name='home'),
    path('teams', teams, name="teams"),
    path("maps/<str:team_id>/", maps, name="maps"),
    ]