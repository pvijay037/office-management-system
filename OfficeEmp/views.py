from django.shortcuts import render, HttpResponse
from . models import Employee, Role, Department
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,"OfficeEmp/index.html")
def Allemp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    print(context)
    return render(request,"OfficeEmp/AllEmp.html",context)
def Addemp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department = request.POST['department']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        role = request.POST['role']
        phone = request.POST['phone']
        hire_data = request.POST['hire_data']
        new_emp = Employee(first_name=first_name, last_name=last_name, department_id=department, salary=salary,
                           bonus=bonus, role_id=role, phone=phone, hire_data=datetime.now())
        new_emp.save()
        return HttpResponse("employee added successfully")
    elif request.method == 'GET':
        return render(request, "OfficeEmp/AddEmp.html")
    else:
        return HttpResponse("an Exception Occur")
def Delemp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("employee deleted successfully")
        except:
            return HttpResponse("please enter a valid employee id")

    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, "OfficeEmp/DelEmp.html", context)

def Filteremp(request):
    return render(request,"OfficeEmp/FilterEmp.html")



