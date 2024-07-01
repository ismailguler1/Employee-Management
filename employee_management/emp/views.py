from django.shortcuts import render, redirect
from .models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

#@login_required decoratoru kullanılarak giriş yapmamış kullanıcıların yönetim paneline erişimi engelleniyor





@login_required
def allemployees(request):
    emp = Employee.objects.all()
    return render(request, "emp/allemployees.html", {"allemployees": emp})

@login_required
def singleemployee(request, empid): 
    return render(request, "emp/singleemployee.html")

@login_required
def addemployee(request):
    if request.method == "POST":
        employeeid = request.POST.get('employeeid')
        employeename = request.POST.get('employeename')
        employeesurname = request.POST.get('employeesurname')
        employeeemail = request.POST.get('employeeemail')
        employeephone = request.POST.get('employeephone')
    
        e = Employee()
        e.employeeid = employeeid
        e.employeename = employeename
        e.employeesurname = employeesurname
        e.email = employeeemail
        e.phone = employeephone
        e.save()
        return redirect("/allemployees")
    return render(request, "emp/addemployee.html")



@login_required
def deleteemployee(request, empid):
    e = Employee.objects.get(pk = empid)
    e.delete()
    return redirect("/allemployees")

@login_required
def editemployee(request, empid):

    e = Employee.objects.get(pk = empid)
    return render(request, "emp/editemployee.html", {"singleemp": e})

@login_required
def doeditemployee(request, empid):
    editedemployeeid      = request.POST.get('employeeid')
    editedemployeename    = request.POST.get('employeename')
    editedemployeesurname = request.POST.get('employeesurname')
    editedemployeeemail   = request.POST.get('employeeemail')
    editedemployeephone   = request.POST.get('employeephone')
    em = Employee.objects.get(pk = empid)
    em.employeeid      = editedemployeeid
    em.employeename    = editedemployeename
    em.employeesurname = editedemployeesurname
    em.email           = editedemployeeemail
    em.phone           = editedemployeephone
    em.save()
    return redirect("/allemployees")