from django.db.models import *
from django.conf import settings
# Create your models here.

class firstdb(Model):
	name = CharField(max_length = 25, primary_key = True)
	email = EmailField(max_length = 25,blank = True)
	ip = GenericIPAddressField(max_length = 20,default = '0.0.0.0')
		