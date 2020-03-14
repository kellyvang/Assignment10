from django.conf.urls import include, url
from django.urls import path
from . import views

# Routes to specific areas on the site
urlpatterns = [
    path('', views.index, name='index'),
    path('allstocks/', views.allstocks, name='allstocks'),
    path('stock/<int:id>', views.stock, name='stock'),    
    path('bond/<int:id>', views.bond, name='bond'),   
    path('charts/', views.chart), 
]