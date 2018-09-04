from django import forms

class Eucledian_f(forms.Form):
	number1 = forms.IntegerField(label = 'Number 1',)
	number2 = forms.IntegerField(label = 'Number 2',)