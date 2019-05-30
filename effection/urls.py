from django.urls import path

from . import views

app_name = 'effection'

urlpatterns = [
    path('', views.index, name='index')
]