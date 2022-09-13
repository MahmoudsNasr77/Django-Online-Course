app_name="about"
from django.urls import path 
from . import views
urlpatterns = [
path('',views.render_about,name="about_render" ),
]