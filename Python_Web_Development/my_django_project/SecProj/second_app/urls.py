from django.urls import path
from second_app import views

urlpatterns = [
    path('',views.Nerd,name='Nerd'),
]
