from django.urls import path
from . import views

urlpatterns = [
    path('',views.hackathon_view ),
    path('search/',views.search_view,name="search_results"),
]
