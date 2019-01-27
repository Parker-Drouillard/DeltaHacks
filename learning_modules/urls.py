from django.urls import path
from . import views


app_name = 'learning_modules'

urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name = 'index'),
    path('learning/', views.learning, name = 'learning')
=======
    path('', views.base, name = 'base'),
    path('learn/', views.learn, name = 'learn'),
    path('compare/', views.compare, name = 'compare'),
    path('connect/', views.connect, name = 'connect'),
>>>>>>> perfectView
]
