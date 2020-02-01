from django.shortcuts import render

def home(request):
	return render(request,'home.html',{})

def answer(request):
	x = request.GET['fulltext'].split(' ')
	return render(request,'answer.html',{'x':len(x)})