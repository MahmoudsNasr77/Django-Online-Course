app_name="course"
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.course_render,name='view_course'),
     path('<str:slug>',views.single_course,name='view_single_course'),
]