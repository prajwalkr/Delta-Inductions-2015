from django.shortcuts import render
from forms import textbox
from django.http import HttpResponse
from os.path import *
def search(request):
	if request.method == "GET":
		form = textbox()
		return render(request,'userform.html',{'form':form})
	else:
		form = textbox(request.POST)
		if form.is_valid():
			find = int(form.cleaned_data.get('number'))
			f = open(join(dirname(__file__),'data.txt'),'r')
			a = map(int,str(f.read()).split())
			f.close()
			pos = bs(a,find)
			if pos == -1:
				return HttpResponse('Number not in file')
			else:
				return HttpResponse('Number found at position: ' + str(pos + 1))
		return HttpResponse('Invalid input. Enter an integer.')

def bs(a,find):
	beg = 0
	last = len(a) - 1
	while beg <= last:
		mid = (beg + last)/2
		if a[mid] == find:
			return mid
		elif a[mid] < find:
			beg = mid + 1
		else:
			last = mid - 1
	return -1
