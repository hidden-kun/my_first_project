from course.serializers import BranchSerializer
import django
from django.http.response import HttpResponseRedirect

from django.shortcuts import render , get_object_or_404, redirect
from django.views.generic.edit import UpdateView
from rest_framework import serializers
from course.forms import GroupForm , BranchForm , StudentForm 
from .models import Branch, Course, Student , Group
from django.views.generic import ListView , DetailView , CreateView

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def my_main_page(request):
    return render(request, 'course/my_page.html')
@login_required
def branch_edit(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    if request.method == "POST":
        form = BranchForm(request.POST, request.FILES , instance=branch)
        if form.is_valid():
            branch = form.save()
            return redirect("branch_detail", branch_id=branch.id)
    else:
        form = BranchForm(instance=branch)

    return render(request, 'course/branch-edit.html', {'form':form})

class BranchUpdateView(LoginRequiredMixin,UpdateView):
    model = Branch
    fields = ['name', 'address', 'photo']
    template_name = 'course/branch-edit.html'
    pk_url_kwarg = 'branch_id'
    login_url = '/user/login/'



def branches_list(request):
    branches=Branch.objects.all
    my_comtex = {'branches': branches}
    return render(request, 'course/branches-list.html', my_comtex) 

class BranchListView(ListView):
    model = Branch
    template_name = 'course/branches-list.html'
    context_object_name = 'branches'


class BranchCreateView(LoginRequiredMixin,CreateView):
    model = Branch
    fields = ['name', 'address', 'photo']
    template_name = 'course/branch_create.html'
    login_url = '/user/login/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


def branch_detail(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    groups = Group.objects.filter(branch=branch)
    context = {'branch': branch, 'groups': groups}

    return render(request,'course/branch_detail.html',context=context)


class BranchDetailView(DetailView):
    model = Branch
    template_name = 'course/branch_detail.html'
    context_object_name = 'branch'
    pk_url_kwarg = 'branch_id'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups']=Group.objects.filter(branch=self.object)
        return context


@login_required
def branch_create(request):
    if request.method == "POST":
        form = BranchForm(request.POST, request.FILES )

        if form.is_valid():
            branch = form.save(commit=False)
            branch.creator = request.user
            branch.save()
            return redirect('branch_detail', branch_id=branch.id)
    else:
        form = BranchForm()

    return render(request, 'course/branch_create.html', {'form': form})


def my_students(request):
    students=Student.objects.all
    my_st = {'students': students}
    return render(request, 'course/students.html', my_st)


class StudentListView(ListView):
    
    model = Student
    template_name = 'course/students.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):

    model =Student
    template_name = "course/student_detail.html"
    context_object_name = 'student'
    pk_url_kwarg = 'student_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(student=self.object)
        return context

class StudentCreateView(LoginRequiredMixin,CreateView):

    model = Student 
    fields = ['name', 'date_of_birth', 'adaress', 'phone_number', 'gander', 'Group', 'photo','course',]
    template_name = 'course/student_create.html'
    login_url = '/user/login/'
    
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class StudentUpdateView(LoginRequiredMixin,UpdateView):

    model = Student
    fields =['name', 'date_of_birth', 'adaress', 'phone_number', 'gander', 'Group', 'photo','course']
    template_name = 'course/student_edit.html'
    pk_url_kwarg = 'student_id'
    login_url = '/user/login/'

@login_required
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.creator = request.user
            student.save()
            return redirect('student_detail', student_id= student.id)
    else:
        form = StudentForm()

    return render(request, 'course/student_create.html', {'form': form})

def student_detail(request, student_id):
    student=Student.objects.get(id=student_id)
    groups=Group.objects.filter(student=student)
    context={'student': student , 'group':groups}
    return render(request,'course/student_detail.html', context = context)

@login_required
def student_edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES , instance=student)
        if form.is_valid():
            student = form.save()
            return redirect("student_detail", student_id=student.id)
    else:
        form = StudentForm(instance=student )

    return render(request, 'course/student_edit.html', {'form':form})



def my_groups(request):
    groups=Group.objects.all
    my_gr = {'groups': groups}
    return render(request,'course/my_groups.html',my_gr)

class GroupListView(ListView):
    model = Group
    template_name = 'course/my_groups.html'
    context_object_name = 'groups'

class GroupDetailView(DetailView):
    model = Group
    context_object_name = 'group'
    template_name = 'course/group_detail.html'
    pk_url_kwarg = 'group_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students']=Student.objects.filter(Group=self.object)
        return context

def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    students = Student.objects.filter(Group=group)
    context = {'group': group, 'students': students}
    return render(request, 'course/group_detail.html', context=context)

class GroupUpdateView(LoginRequiredMixin,UpdateView):
    model = Group
    fields = ['name', 'branch', 'photo']
    template_name = 'course/group_edit.html'
    pk_url_kwarg = 'group_id'
    login_url = '/user/login/'

@login_required
def group_edit(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == "POST":
        form = GroupForm(request.POST,request.FILES, instance=group)
        if form.is_valid():
            group = form.save()
            return redirect("group_detail", group_id=group.id)
    else:
        form = GroupForm(instance=group )

    return render(request, 'course/group_edit.html', {'form':form})

@login_required
def group_create(request):
    if request.method == "POST":
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            group = form.save(commit=False)
            group.creator = request.user
            group.save()
            
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupForm()

    return render(request, 'course/group_create.html', {'form': form})


class GroupCreateView(LoginRequiredMixin,CreateView):
    
    model = Group
    fields = ['name', 'branch', 'photo']
    template_name= 'course/group_create.html'
    login_url = '/user/login/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



class BranchAPIView(APIView):

    def get(self, request, format=None):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
       
       
        return  Response(serializer.data, status=status.HTTP_200_OK)
        