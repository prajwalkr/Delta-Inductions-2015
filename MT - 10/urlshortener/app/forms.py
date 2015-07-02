from django.forms import *

class urlform(Form):
	link = URLField(label = 'Enter link to shorten:',required = True)