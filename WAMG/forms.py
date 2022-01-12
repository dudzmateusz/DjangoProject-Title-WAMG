from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import admin
from django import forms
from WAMG.models import things


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class AddThingsForm(forms.ModelForm):
	class Meta:
		model = things
		fields = ['name', 'sku', 'ean', 'color','place','quantity','date_add','note','user','photo']
		widgets = {
			'user': forms.HiddenInput(),
			'date_add': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select a date',
														  'type': 'date', 'background':'black'}) }

		def __init__(self, *args, **kwargs):
			self.name = kwargs.pop('name')
			super(AddThingsForm, self).__init__(*args, **kwargs)

			name = forms.CharField()

			if name is not None:
				self.fields['name'] = forms.CharField(initial=self.name)
