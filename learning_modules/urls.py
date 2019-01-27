from django.urls import path
from . import views


app_name = 'learning_modules'

urlpatterns = [
    path('', views.base, name = 'base'),
    path('learn/', views.learn, name = 'learn'),
]
