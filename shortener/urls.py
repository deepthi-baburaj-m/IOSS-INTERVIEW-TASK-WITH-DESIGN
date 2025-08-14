from django.urls import path
from . import views

urlpatterns = [
    #Urls 
    path('', views.index, name='index'),
    path('<str:shorter_url>/', views.redirect_url, name='redirect'),
]