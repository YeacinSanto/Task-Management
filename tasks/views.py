from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import *
from datetime import date
from django.db.models import Q,Count, Max, Min

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
    # task_count = Task.objects.aggregate(num_task=Count("id"))
    # tasks = Task.objects.prefetch_related("assigned_to").all()
   
    task_count = Project.objects.annotate(num_task=Count("task"))
    
    return render(request, "show_task.html",{"task_count":task_count})