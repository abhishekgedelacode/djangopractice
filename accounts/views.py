from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.


def index(request):
    return HttpResponse("<h1>hello world <hr/> smart code </h1>")


def display(request):
    context = {}
    context['dataset'] = Student.objects.all()
    return render(request, 'accounts/display.html', context)
