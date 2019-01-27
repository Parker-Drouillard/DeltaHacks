from django.urls import path
from . import views


app_name = 'learning_modules'

urlpatterns = [

    path('index/', views.index, name = 'index'),
    path('learning/', views.learning, name = 'learning'),
    path('compare/', views.compare, name = 'compare'),
    path('compare-info/', views.compare_info_form, name='compare_info_form')

]
