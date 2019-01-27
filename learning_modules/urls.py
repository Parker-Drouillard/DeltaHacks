from django.urls import path
from . import views


app_name = 'learning_modules'

urlpatterns = [

    path('', views.index, name = 'index'),
    path('learning/', views.learning, name = 'learning'),
    path('compare/', views.compare, name = 'compare'),
    path('connect/', views.connect, name = 'connect'),

]
