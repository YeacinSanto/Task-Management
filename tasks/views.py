from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm, TaskDetailModelForm
from tasks.models import *
from datetime import date
from django.db.models import Q,Count, Max, Min
from django.contrib import messages

# Create your views here.

def manager_dashboard(request):
    
    type = request.GET.get("type", "all")
    
    
    
    
    
    
    counts = Task.objects.aggregate(
        total=Count("id"),
        completed = Count("id",filter=Q(status="COMPLETED")),    
        in_progress = Count("id",filter=Q(status="IN_PROGRESS")),    
        pending = Count("id",filter=Q(status="PENDING")),  
    )
    
    # retrieving task data
    base_query = Task.objects.select_related("Details").prefetch_related("assigned_to")
    
    if type == "completed":
        tasks = base_query.filter(status="COMPLETED")
    elif type == "in-progress":
        tasks = base_query.filter(status="IN_PROGRESS")
    elif type == "pending":
        tasks = base_query.filter(status="PENDING")
    elif type == "all":
        tasks = base_query.all()
    
    context = {
        "tasks": tasks,
        "counts" : counts
    }
    
    return render(request, "dashboard/manager_dashboard.html", context)


def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html")

def test(request):
    context = {
        "names" : ["Mahmud", "Ahmed", "Jhon"]
    }
    return render(request, "test.html" ,context)


def create_task(request):
    # employees = Employee.objects.all()
    form = TaskModelForm() #for GET
    task_detail_form = TaskDetailModelForm()
    
    if request.method == "POST":
        form = TaskModelForm(request.POST) #for post
        task_detail_form = TaskDetailModelForm(request.POST)
        
        if task_detail_form.is_valid() and form.is_valid():
            
            '''For Model form Data'''
            task = form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()
            
            messages.success(request,"Task created successfully")
            return redirect("create-task")
            
            
    context = {"task_form":form, "task_detail_form":task_detail_form}
    return render(request, "task_form.html",context)

def update_task(request,id):
    
    task = Task.objects.get(id=id)
    
    form = TaskModelForm(instance=task) #for GET
    
    if task.Details:
        task_detail_form = TaskDetailModelForm(instance=task.Details)
    
    if request.method == "POST":
        form = TaskModelForm(request.POST, instance=task) #for post
        task_detail_form = TaskDetailModelForm(request.POST, instance=task.Details)
        
        if task_detail_form.is_valid() and form.is_valid():
            
            '''For Model form Data'''
            task = form.save()
            task_detail=task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()
            
            messages.success(request,"Task updated successfully")
            return redirect("update-task",id)
            
            
    context = {"task_form":form, "task_detail_form":task_detail_form}
    return render(request, "task_form.html",context)


def delete_task(request, id):
    if request.method == "POST":
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, "Task deleted successfully")
        return redirect("manager-dashboard")
    else:
        messages.error(request, "Something went wrong")
        return redirect("manager-dashboard")


def view_task(request):
    # task_count = Task.objects.aggregate(num_task=Count("id"))
    # tasks = Task.objects.prefetch_related("assigned_to").all()
   
    task_count = Project.objects.annotate(num_task=Count("task"))
    
    return render(request, "show_task.html",{"task_count":task_count})