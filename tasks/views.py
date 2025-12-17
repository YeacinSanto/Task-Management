from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee,Task
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
    # retrive all data from task app
    tasks = Task.objects.all()
    
    # retrive a specific task
    task_3 = Task.objects.get(id=1)
    
    return render(request, "show_task.html",{"tasks":tasks, "task3":task_3})