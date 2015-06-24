from django.http import HttpResponse
from django.shortcuts import render
from forms import userform
from .models import firstdb

# Create your views here.
def check(name):
	# 1. No special chars
	for i in name:
		if i != ' ' and ord(i) < 65 or ord(i) > 122:
			return False
def process_form(request):
	if request.method == 'POST':
		form = userform(request.POST)
		if form.is_valid() == True:
			name = form.cleaned_data.get('name')
			if check(name) == False:
				return HttpResponse("Invalid submission at the name field.")
			email = form.cleaned_data.get('email')
			ip = form.cleaned_data.get('ip')
			p = firstdb(name,email,ip)
			p.save()
			return render(request, 'user_submit.html', {'name':name,'email':email,'ip':ip})
		return HttpResponse("Invalid submission. Check one or more fields.")
	elif request.method == 'GET':
		form = userform()
		return render(request, 'user_form.html', {'form':form})

