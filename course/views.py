from multiprocessing import context
from django.shortcuts import render
from .models import courses,comments

def course_render(request):
    courses_list=courses.objects.all()
    return render(request,'Course_list.html',{'courses_list':courses_list})
def single_course(request,slug):
    course=courses.objects.get(slug=slug)
    context={'course':course}
    return render(request,'Single_Course.html',context)
