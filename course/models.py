from django.db import models
from django.db.models.base import Model
from django.urls import reverse
from django.conf import settings

# Create your models here.



class Branch(models.Model):
    class Meta:
        verbose_name = 'филиал'
        verbose_name_plural = 'филиалы' 

    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=300, null=True)
    photo = models.ImageField(upload_to='branches/', null=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.PROTECT, null=True, related_name='branches')
    manger = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ("branch_detail", kwargs={"branch_id": self.pk})


class Group(models.Model):
    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
    name = models.CharField(max_length=100, null=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='groups/', null=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.PROTECT, null=True)
    course = models.ForeignKey('course.Course', on_delete=models.PROTECT, null=True)



    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ("group_detail", kwargs={"group_id": self.pk})

class Course(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self): 
        return self.name


class Student(models.Model):

    MALE = 'male'
    FAMALE = 'female'
    GENDER_CHOICES = (
        (MALE,'male'),
        (FAMALE, 'famale'),

    )

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
    name = models.CharField(max_length=200, null=False)
    date_of_birth = models.DateField(null=False)
    adaress = models.CharField(max_length=300, null=True, blank=True)
    phone_number =models.CharField(max_length=20, null= False)
    gander = models.CharField(choices=GENDER_CHOICES, max_length=6, default=MALE)
    Group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    photo = models.ImageField(upload_to='students/', null=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.PROTECT, null=True)

    course = models.ManyToManyField(Course)
    age= models.PositiveBigIntegerField(null=True)
    



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ("student_detail", kwargs={"student_id": self.pk})
