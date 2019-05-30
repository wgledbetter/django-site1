from django.urls import path

from . import views

app_name = 'astro'

urlpatterns = [
    path('', views.index, name='index')
]