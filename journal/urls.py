from django.urls import path

from . import views

app_name = 'journal'

urlpatterns = [
    path('all/', views.all, name='all'),
    path('', views.index, name='index'),
    # path('food/', views.food, name='food'),
    path('<int:year>/', views.year, name='year'),
    path('<int:year>/<int:month>/', views.year_month, name='year_month'),
    path('<int:year>/<int:month>/<int:day>/', views.year_month_day, name='year_month_day'),
    path('<slug:jname>/', views.journal, name='journal-detail'),
    path('entry/<uuid:euuid>', views.entry, name='entry'),
]