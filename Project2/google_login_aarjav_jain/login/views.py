from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def home(request):
    return render(request, loader.get_template('home.html'))
	#return render(request, 'login/home.html', {})
	#return HttpResponse('Hello')

def login(request):
    return HttpResponse('Hello Login')
