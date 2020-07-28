from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from django.forms import ModelForm

from delivery.models import User, Store, Order, Driver


class StoreSignUpForm(UserCreationForm):
    adder = forms.CharField(label='عنوان المتجر بالكامل')
    name = forms.CharField(label='اسم المتجر')
    phone = forms.CharField(label='رقم الجوال')
    password1 = forms.CharField(
        label=("كلمة السر"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("تأكيد كلمة السر"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )

    class Meta(UserCreationForm.Meta):
        model = User


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_store = True
        user.phone = self.cleaned_data['phone']
        user.save()
        store = Store.objects.create(user=user)
        store.adder = self.cleaned_data['adder']
        store.name = self.cleaned_data['name']
        store.save()
        return user


class DriverSignUpForm(UserCreationForm):
    city = forms.CharField(label='المدينة')
    name = forms.CharField(label='الأسم بالكامل')
    phone = forms.CharField(label='رقم الجوال')
    password1 = forms.CharField(
        label=("كلمة السر"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("تأكيد كلمة السر"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )

    class Meta(UserCreationForm.Meta):
        model = User


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_driver = True
        user.phone = self.cleaned_data['phone']
        user.save()
        driver = Driver.objects.create(user=user)
        driver.city = self.cleaned_data['city']
        driver.name = self.cleaned_data['name']
        driver.save()
        return user