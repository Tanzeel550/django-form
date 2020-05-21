from django.shortcuts import render, HttpResponse
from EmployeeForm.forms import EmployeeForm
from EmployeeForm import models

# Create your views here.
def index(request):
    return render(request, 'EmployeeForm/index.html')

def form(request):
    form = {'form': EmployeeForm}

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("<h1> Thank you for using our service.We will contact you soon </h1>")

    form = {'form': EmployeeForm}
    return render(request, 'EmployeeForm/form.html', context=form)


def employee_list(request):
    d = models.Employee_Model.objects.order_by('name')
    d = {'d':d}
    return render(request, 'EmployeeForm/employee_list.html', context=d)
