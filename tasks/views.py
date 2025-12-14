from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm
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
    form = TaskForm(employees=employees) #for GET
    
    if request.method == "POST":
        form = TaskForm(request.POST,employees=employees)
        if form.is_valid():
            data = form.cleaned_data
            title = data.get("title")
            description = data.get("description")
            due_date = data.get("due_date")
            assigned_to = data.get("assigned_to")
            
            task = Task.objects.create(title=title, description=description, due_date=due_date)
            
            # assign employee to task
            for emp_id in assigned_to:
                employee = Employee.objects.get(id = emp_id)
                task.assigned_to.add(employee)
            
            return HttpResponse("Task Added successfully")
            
    context = {"form":form}
    return render(request, "task_form.html",context)