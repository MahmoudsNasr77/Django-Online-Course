from multiprocessing import context
from re import I
from django.shortcuts import render
from .models import Instructor
from django.core.paginator import Paginator
def view_instructos(request):
    instructor_list=Instructor.objects.all()
    paginator = Paginator(instructor_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  
    context={'instructor':page_obj,'instructor_list':instructor_list}
    return render(request,'Instructors_list.html',context)
def view_instructor(request,slug):
    instructor=Instructor.objects.get(slug=slug)
    
    context={'instructor':instructor}
    return render(request,'single_Instructor.html',context)