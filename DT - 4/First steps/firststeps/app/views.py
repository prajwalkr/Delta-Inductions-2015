from django.http import HttpResponse
from django.shortcuts import render
from forms import userform
from .models import firstdb
from heapq import *
from collections import defaultdict
import operator
# Create your views here.
def check(name):
	# 1. No special chars
	for i in name:
		if i != ' ' and ord(i) < 65 or ord(i) > 122:
			return False
def process_form(request):
	if request.method == 'POST':
		form = userform(request.POST,request.FILES)
		if form.is_valid() == True:
			name = form.cleaned_data.get('name')
			if check(name) == False:
				return HttpResponse("Invalid submission at the name field.")
			email = form.cleaned_data.get('email')
			ip = form.cleaned_data.get('ip')
			txtfile = request.FILES['txtfile']
			txtfile = compress(txtfile)
			p = firstdb(name,email,ip)
			p.save()
			return render(request, 'user_submit.html', {'name':name,'email':email,'ip':ip,'filedata':txtfile})
		return HttpResponse("Invalid submission. Check one or more fields.")
	elif request.method == 'GET':
		form = userform()
		return render(request, 'user_form.html', {'form':form})

def encode(freq):
    heap = [[count, [char, '']] for char, count in freq.items()]
    heapify(heap)
    while len(heap) >= 2:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    res = heappop(heap)[1:]
    res = sorted(res, key = operator.itemgetter(0))
    code = ""
    for pair in res:
        code += pair[1]
    return code

def compress(txtfile):
	text = txtfile.read()
	freq = defaultdict(int)
	for letter in text:
		freq[letter] += 1
	MEDIA_ROOT = 'C:/Users/Prajwal K R/Desktop/First steps/firststeps/media/'
	compressed_file = MEDIA_ROOT + 'compressed_file.txt'
	compress = open(compressed_file,'w+')
	compress.write(encode(freq))
	data = compress.read()
	compress.close()
	return data
