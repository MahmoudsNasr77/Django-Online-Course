app_name='Instructors'
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.view_instructos,name='view_instructos'),
     path('<str:slug>',views.view_instructor,name='view_instructor'),
]