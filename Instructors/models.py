from email.mime import image
from django.db import models
from django.utils.text import slugify
class categeory(models.Model):
    name=models.CharField(max_length=50 ,null=False,blank=False)
    def __str__(self):
        return self.name
class Instructor(models.Model):
    name=models.CharField(max_length=50 ,null=False,blank=False)
    job=models.CharField(max_length=50,blank=True, null=True)
    image=models.ImageField(upload_to='Instructor_image')
    slug = models.SlugField(null=True,blank=True) 
    categeory=models.ForeignKey("categeory",on_delete=models.CASCADE,null=True,blank=True)
    facebook = models.URLField(default="https://www.facebook.com/")
    linkdin = models.URLField(default="https://www.linkedin.com/")
    github = models.URLField(default="https://github.com/")
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Instructor,self).save(*args,**kwargs)
    def __str__(self):
        return self.name
    
