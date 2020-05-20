from django.shortcuts import render
from EmployeeForm.forms import EmployeeForm
from EmployeeForm import models


# Create your views here.
def index(request):
    return render(request, 'EmployeeForm/index.html')

def form(request):
    form = {'form': EmployeeForm}
    print("Hooooooooooooooooooo")

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data['name'])
            # for key, value in form.cleaned_data:
                # print(key, ' : ', value)
            form.save(commit=True)
            print("DFSAAAAAAAAAAA")
    else:
        print("allah kaam bana de")

    form = {'form': EmployeeForm}
    return render(request, 'EmployeeForm/form.html', context=form)

def employee(request):
    return render(request, 'EmployeeForm/employee.html')

def display_employee(request):
    d = models.Employee_Model.objects.order_by('name')
    d = {'d':d}
    return render(request, 'EmployeeForm/employee.html', context=d)
