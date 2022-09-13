from multiprocessing import context
from django.shortcuts import render
from Instructors.models import Instructor
def home_render(request):
    instructor_list=Instructor.objects.all()
    context={"instructor_list":instructor_list}
    return render(request,'index.html',context)
