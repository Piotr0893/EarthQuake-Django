from django.urls import path 
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('Last24Hours', views.Last24Hours, name ='Last24Hours'),
    path("Last1Hour", views.Last1Hour, name='Last1Hour'),
    path('Last7Days', views.Last7Days, name='Last7Days'), 
]
