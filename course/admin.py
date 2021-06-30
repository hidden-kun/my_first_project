from course.models import Branch

from .models import Branch, Course, Group, Student
from django.contrib import admin

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',)
    search_fields =('name', 'address',)
    list_filter =('creator', 'manger', )
    raw_id_fields = ('creator', )



admin.site.register(Branch, BranchAdmin)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Course)
# Register your models here.
