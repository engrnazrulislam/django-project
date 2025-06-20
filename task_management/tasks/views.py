from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1 style='color: navy; text-align:center'>Welcome to the task management system</h1>")
def contact(request):
    return HttpResponse("<h1 style='color:red'>Maintenance Engineer, Dept. of CSE, DUET</h>")
def show_tasks(request):
    return HttpResponse("<h1 style='color:red'>Your tasks</h>")