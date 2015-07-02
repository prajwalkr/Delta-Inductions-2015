from django.shortcuts import render
from forms import urlform
from models import url
from django.http import HttpResponse
# Create your views here.
charmap = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def shorten(request):
	if request.method == 'POST':
		form = urlform(request.POST)
		if form.is_valid() == True:
			link = form.cleaned_data.get('link')
			p = url(link)
			short = shortened(link)
			p.save()
			return render(request, 'user_submit.html', {'link':link,'short':short})
		return HttpResponse("Invalid submission. Check one or more fields.")
	elif request.method == 'GET':
		form = urlform()
		return render(request, 'user_form.html', {'form':form})

def shortened(link):
	prev_id = open('prev_id.txt','r+')
	id = int(prev_id.read())
	base62 = []
	temp = id
	while temp > 0:
		base62.append(temp%62)
		temp /= 62
	suffix = ''
	for i in base62:
		suffix += charmap[i]
	prev_id.seek(0)
	prev_id.truncate()
	prev_id.write(str(id + 1))
	prev_id.close()
	return 'www.praj.wal/' + suffix

