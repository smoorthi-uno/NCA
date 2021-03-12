from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, UpdateView
from ..forms import StaffsSignUpForm, VolunteerSignUpForm
from ..models import Volunteer, User


class VolunteerSignUpView(CreateView):
    model = User
    form_class = VolunteerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'volunteer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('admins:signup')


class volunteer_home(ListView):
    model = Volunteer
    template_name = 'volunteer/volunteer.html'
