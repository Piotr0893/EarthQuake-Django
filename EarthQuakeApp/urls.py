from django.urls import path 
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('Last24Hours', views.Last24Hours, name ='Last24Hours'),
    path("Last1Hour", views.Last1Hour, name='Last1Hour'),
    path('Last7Days', views.Last7Days, name='Last7Days'), 
    path('Last24hMap', views.Last24hMap, name ='Last24hMap'),
    path('Last1hMap', views.Last1hMap, name ='Last1hMap'),
    path('Last7dMap', views.Last7dMap, name ='Last7dMap'),
]
