from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .models import Student
from .forms import Stdform

# Create your views here.


def index(request):
    return HttpResponse("<h1>hello world <hr/> smart code </h1>")


def display(request):
    context = {}
    context['dataset'] = Student.objects.all()
    return render(request, 'accounts/display.html', context)


def create_view(request):
    context = {}
    form = Stdform(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context['form'] = form
    return render(request, 'accounts/create_view.html', context)
