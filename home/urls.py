
app_name='home'
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home_render,name='home_render'),
]