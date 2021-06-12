from django import forms


class EmployeeInfoForm(forms.Form):
    name = forms.CharField(max_length = 50)
    salary = forms.IntegerField()
    age = forms.IntegerField()
    
