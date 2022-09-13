from distutils.command.upload import upload
from email.policy import default
from django.db import models
from Instructors.models import Instructor
from django.contrib.auth.models import User
from django.utils.text import slugify
class courses(models.Model):
    instructor_name=models.ForeignKey(Instructor,related_name="Course_instructor",on_delete=models.CASCADE)
    course_name=models.CharField(max_length=150)
    course_price=models.IntegerField(default=0)
    course_houre=models.IntegerField(default=0)
    course_Student=models.IntegerField(default=0)
    slug = models.SlugField(null=True,blank=True)  
    course_image=models.ImageField(upload_to="course_image",default="image.png" )
    course_rate=models.DecimalField(max_digits=5, decimal_places=1,default=0.0)
    def __str__(self):
        return self.course_name
    def save(self,*args,**kwargs):
        self.slug=slugify(self.course_name)
        super(courses,self).save(*args,**kwargs)
class comments(models.Model):
    courses=models.ForeignKey(courses,related_name="comment_course",on_delete=models.CASCADE)
    comment_owner=models.ForeignKey(User,related_name='comment_owner',on_delete=models.CASCADE)
    data=models.DateTimeField(auto_now_add=True)
    comment=models.TextField(max_length=1500)

    
