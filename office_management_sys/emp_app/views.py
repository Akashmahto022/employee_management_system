from django.shortcuts import render
from .models import Employee, Department, Role
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    return render(request, 'all_emp.html', {'emps': emps})


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        hire_date = request.POST['hire_date']
        new_emp = Employee(first_name = first_name, last_name = last_name, dept_id = dept, salary= salary, bonus = bonus, role_id= role, phone=phone, hire_date=hire_date)
        new_emp.save()
        return redirect('all_emp')
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    
    else:
        return render(request, 'add_emp.html')


def remove_emp(request):
    return render(request, 'remove_emp.html')


def filter_emp(request):
    return render(request, 'filter_emp.html')