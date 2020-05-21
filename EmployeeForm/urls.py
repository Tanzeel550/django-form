from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from EmployeeForm import views

app_name = 'form_app'

urlpatterns = [
    url(r'^$', views.form, name='form'),
    url(r'^employee_list/$', views.employee_list, name='employee_list'),
    path('admin/', admin.site.urls),
]