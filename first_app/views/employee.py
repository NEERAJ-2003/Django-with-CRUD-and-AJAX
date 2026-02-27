from django.shortcuts import render, get_object_or_404
from first_app.models import Employee
from first_app.forms import EmployeeForm


def employee_list(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")

    employees = Employee.objects.all()
    return render(request, "employee_list.html", {"employees": employees})


def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return employee_list(request)
    else:
        form = EmployeeForm()

    return render(request, "employee_form.html", {"form": form})


def employee_update(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return employee_list(request)
    else:
        form = EmployeeForm(instance=employee)

    return render(request, "employee_update.html", {"form": form})


def employee_delete(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)

    if request.method == "POST":
        employee.delete()
        return employee_list(request)

    return render(request, "employee_delete.html", {"employee": employee})


def employee_detail(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    return render(request, "employee_detail.html", {"employee": employee})