from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



def homepage(request):
    return render(request, 'info.htm')