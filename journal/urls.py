from django.urls import path

from . import views

app_name = 'journal'

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.index, name='index'),
    path('food/', views.food, name='food'),
]