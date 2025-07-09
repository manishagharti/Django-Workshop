from django.shortcuts import render
from django.http import HttpResponse
from employee.models import Employee


def home(request):
    return render(request, 'home.html')


def contact(request):
    employee = Employee.objects.all()
    context = {
        'employee': employee
    
    }
    print("data from view",employee)
    return render(request, 'contact.html', context)
