from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Task Management System")



def contact(request):
    return HttpResponse("This is contact page")

def show_task(request):
    return HttpResponse("This is task page")