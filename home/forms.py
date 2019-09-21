from django import forms
from django.contrib.auth.models import User

class Custom_login_form(forms.ModelForm):
	"""docstring for Custom_login_form"""
	class Meta:
		model=User
		fields=['username','password']
		widgets={
			'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
			'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
		}
		