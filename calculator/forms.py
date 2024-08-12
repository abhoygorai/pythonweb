from django import forms

class AddForm(forms.Form):
    num1 = forms.IntegerField(label='First Number')
    num2 = forms.IntegerField(label='Second Number')
