from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator

# Create your models here.

class Table(models.Model):

	# General Info Fields
	date            = models.DateTimeField(auto_now_add=True)
	food_id         = models.CharField(max_length=50, blank=False)
	name            = models.CharField(max_length=50, blank=False)
	regular_price   = models.DecimalField(max_digits=99, decimal_places=3, blank=True)
	current_price   = models.DecimalField(max_digits=99, decimal_places=3, blank=True)
	delivery_charge = models.DecimalField(max_digits=99, decimal_places=3, blank=True)
	other_charge    = models.DecimalField(max_digits=99, decimal_places=3, blank=True)
	image           = models.FileField(max_length=100, blank=True)

	status          = models.CharField(validators=[RegexValidator], max_length=50, default='active') #option-> active, inactive 
	
	# Backup Fields
	trash           = models.BooleanField(default=False)
	
	def __str__(self):
		return self.food_id
