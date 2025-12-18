from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import *
from datetime import date
from django.db.models import Q

# Create your views here.

def manager_dashboard(request):
    return render(request, "dashboard/manager_dashboard.html")


def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html")

def test(request):
    context = {
        "names" : ["Mahmud", "Ahmed", "Jhon"]
    }
    return render(request, "test.html" ,context)


def create_task(request):
    employees = Employee.objects.all()
    form = TaskModelForm() #for GET
    
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            
            '''For Model form Data'''
            form.save()
            
            return render(request,"task_form.html",{"form":form, "message":"task added successfully"})
            
            
    context = {"form":form}
    return render(request, "task_form.html",context)

def view_task(request):
    # show the task based on status
    # tasks = Task.objects.filter(status="PENDING")
    
    # show the task based on date
    # tasks = Task.objects.filter(due_date = date.today())
    
    # show the task that priority not low
    # tasks = TaskDetail.objects.exclude(priority="L")
    
    '''show task that contain specific word with and(,)'''
    
    # tasks = Task.objects.filter(title__icontains="c",status="PENDING")
    
    '''Task with or condition'''
    # tasks = Task.objects.filter(Q(status="PENDING") | Q(status="IN_PROGRESS"))
    
    """Advance"""
    # select_related (foreign_key, OneToOneField)
    # tasks = TaskDetail.objects.select_related("task").all()
    
    # foreign key
    # tasks = Task.objects.select_related("project").all()
    # in select_related works one way in manytomany field. but not work in both way
    '''prefetch_related(reverse foreign key, manytomany)'''
    # tasks = Project.objects.prefetch_related("task_set").all()
   
    # how many employee in a specific task
    tasks = Task.objects.prefetch_related("assigned_to").all()
    
    return render(request, "show_task.html",{"tasks":tasks})