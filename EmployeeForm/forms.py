from django import forms
from django.forms import ModelForm
from EmployeeForm.models import Employee_Model
from datetime import date

gender_choices = [
    ('M','Male'),('F',"Female"),('B', 'both')
]

def check_email(value):
    if value.endswith('.com') == False:
        raise forms.ValidationError("Oops! you have typed wrong email address.")

class EmployeeForm(ModelForm, forms.Form):
    name = forms.CharField(max_length = 26, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : 'Name'
    }))
    address = forms.CharField(max_length = 50, widget = forms.TextInput(attrs = {
        'class' :"form-control",
        'placeholder' : 'Address'
    }))
    city = forms.CharField(initial = 'tanzeel',max_length = 16, widget = forms.TextInput(attrs = {
        'class' :"form-control",
        'placeholder' : 'City'
    }))
    state = forms.CharField(initial = 'tanzeel',max_length = 16, widget = forms.TextInput(attrs = {
        'class' :"form-control",
        'placeholder' : 'State'
    }))
    zip_code = forms.IntegerField(initial = 92 ,widget = forms.NumberInput(attrs = {
        'class' :"form-control",
        'placeholder' : 'Zip code'
    }))
    # REMEMBER : must end with .com
    email = forms.EmailField(initial = 'tanzeel@gjl.com', validators = [check_email], widget = forms.EmailInput(attrs = {
        'class' :"form-control",
        'placeholder' : 'Email'
    }))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class' :"form-control",
        'placeholder' : 'Password'
    }))
    social_security = forms.CharField(initial = 'tanzeel',max_length = 26, widget = forms.TextInput(attrs = {
        'class' :"form-control",
        'placeholder' : 'Social Security'
    }))
    hire_date = forms.DateField(initial = date.today, widget = forms.DateInput(attrs = {
        'class' :"form-control",
        'placeholder' : 'Hire Date'
    }))
    birth_date = forms.DateField(initial = date.today,widget = forms.DateInput(attrs = {
        'class' :"form-control",
        'placeholder' : 'Birth Date'
    }))
    hourly_rate = forms.DecimalField(min_value=0, max_value=100, initial = 0.9, widget = forms.NumberInput(attrs = {
        'class' :"form-control",
        'placeholder' : 'Hourly Rate'
    }))
    title = forms.CharField(initial = 'tanzeel',max_length = 26, widget = forms.TextInput(attrs = {
        'class' :"form-control",
        'placeholder' : 'Title of job'
    }))
    status = forms.CharField(initial = 'tanzeel',max_length = 26, widget = forms.TextInput(attrs = {
        'class' :"form-control",
        'placeholder' : 'Status'
    }))
    gender = forms.ChoiceField(choices = gender_choices, widget = forms.Select(attrs = {
        'class' :"form-control",
        'placeholder' : 'Gender'
    }))
    worked_before = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class' :"form-control form-check-input",
    }))

    class Meta:
        model = Employee_Model
        fields = '__all__'



