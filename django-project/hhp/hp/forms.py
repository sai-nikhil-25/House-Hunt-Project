from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordResetForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User

from .models import Customer,BookAppointment

class LoginForm(AuthenticationForm):
      username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
      password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))


class Meta:
    model = User
    fields = ['username','email','password1','password2']

class MyPasswordChangeForm(PasswordChangeForm):
     old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'autofocus': 'True','autocomplete':'current-password','class':'form-control'}))
     new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
     new_password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
     

class SetPasswordForm(SetPasswordForm):
     new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
     new_password2 = forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
     
class Profile(forms.ModelForm):
     class Meta:
          model = Customer
          fields = ['name','city','mobile','state','zipcode']
          widgets={
               'name':forms.TextInput(attrs={'class':'form-control'}),
               'city':forms.TextInput(attrs={'class':'form-control'}),
               'mobile':forms.NumberInput(attrs={'class':'form-control'}),
               'state':forms.TextInput(attrs={'class':'form-control'}),
               'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
          }
class Appointment(forms.ModelForm):
    listing_title = forms.CharField(label="Title",max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_name = forms.CharField(label="Name",max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_phone = forms.CharField(label="Phone",max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_email = forms.EmailField(label="Email",required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = BookAppointment
        fields = ['appointment_date', 'agree_termsConditions']
        labels = {
            'appointment_date': 'Appointment Date',
            'agree_termsConditions': 'Terms & Conditions'
        }
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'agree_termsConditions': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        help_texts = {
            'agree_termsConditions': 'I agree to the terms and conditions'
        }


