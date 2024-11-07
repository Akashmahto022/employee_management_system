from django.shortcuts import render
from .models import Employee, Department, Role
from django.shortcuts import redirect
from django.db.models import Q

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
    else:
        return render(request, 'add_emp.html')


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_delete = Employee.objects.get(id=emp_id)
            emp_to_be_delete.delete()
        except Exception as e:
            raise e
    emp = Employee.objects.all()
    return render(request, 'remove_emp.html', {'emp':emp})


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        
        if name:
            emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
            
        return render(request, 'all_emp.html', {'emps': emps})
    
    else:
        return render(request, 'filter_emp.html')