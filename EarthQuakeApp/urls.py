from django.urls import path 
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('EarthQuakes', views.Last24EarthQuakes, name ='EarthQuakes'),
    path("Last1Hour", views.Last1Hour, name='Last1Hour'),
    path('Last7Days', views.Last7days, name='Last7Days')
    
    
]