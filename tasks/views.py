from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import *
from datetime import date

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
    tasks = TaskDetail.objects.exclude(priority="L")
    
    return render(request, "show_task.html",{"tasks":tasks})