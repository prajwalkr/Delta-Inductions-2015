from django.forms import *

class userform(Form):
	name = CharField(max_length = 25)
	email = EmailField(max_length = 25)
	ip = GenericIPAddressField(max_length = 20)
	txtfile = forms.FileField(label = 'Select a file')
	