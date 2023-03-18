from django.db import models
from django.urls import reverse


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('collegestoreapp:wikisearch', args=[self.slug])

class Course(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    seats=models.IntegerField()
    available_seats=models.BooleanField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return '{}'.format(self.name)

class person(models.Model):
    name=models.CharField(max_length=250,unique=True,blank=True)
    slug = models.SlugField(max_length=250, unique=True,blank=True)
    Date_of_birth=models.DateField(blank=True)
    Age=models.IntegerField(blank=True, default=None)
    gender=models.CharField(max_length=6,blank=True,default=None)
    phone_number=models.IntegerField(blank=True, default=None)
    mail_id=models.EmailField(blank=True, default=None)
    address=models.TextField(blank=True, default=None)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,blank=True, default=None)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,blank=True, default=None)
    purpose=models.CharField(max_length=20,blank=True, default=None)
    material=models.CharField(max_length=20,blank=True,default=None)

    class Meta:
        ordering = ('name',)
        verbose_name = 'person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        return '{}'.format(self.name)


