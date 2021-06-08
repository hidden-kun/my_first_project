from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.db.models.expressions import F

# Create your models here.



class Branch(models.Model):
    class Meta:
        verbose_name = 'branch'
        verbose_name_plural = 'branches' 

    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
    name = models.CharField(max_length=100, null=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)


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

    def __str__(self):
        return self.name  