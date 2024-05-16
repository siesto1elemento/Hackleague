from django.urls import path
from . import views

urlpatterns = [
    path('',views.hackathon_view ),
]
