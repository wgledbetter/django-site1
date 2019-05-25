from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test, name='Journal Test'),
    path('', views.index, name='Journal Index'),
    path('food/', views.food, name='Food Journal'),
]