from django.shortcuts import render
from django.http import HttpResponse
from formApp import forms

# Create your views here.
def empDetails(request):
    form = forms.EmployeeInfoForm()
    empInfo = {'form':form}
    return render(request,'input.html' , context = empInfo)