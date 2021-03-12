from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.utils import timezone
from nca.models import (User, Staff, Volunteer, Activity)


class StaffsSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staffs = True
        if commit:
            user.save()
            staff = Staff.objects.create(user=user)
        return user


class VolunteerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_volunteer = True
        user.save()
        volunteer = Volunteer.objects.create(user=user)
        return user


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = (
            'staff', 'volunteer', 'victim', 'location', 'name', 'description', 'type', 'start_date', 'end_date', 'created_date', 'updated_date',
            'notes')
