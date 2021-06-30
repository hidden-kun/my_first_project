from django import forms
from django.forms import fields
from course.models import Branch, Group, Student


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('name', 'address', 'photo')

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'branch' , 'photo',)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'date_of_birth', 'adaress', 'phone_number', 'gander', 'Group', 'photo', 'course',)