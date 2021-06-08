from course.models import Branch

from .models import Branch, Group, Student
from django.contrib import admin


admin.site.register(Branch)
admin.site.register(Group)
admin.site.register(Student)

# Register your models here.
