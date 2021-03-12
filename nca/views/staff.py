from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, UpdateView
from ..forms import StaffsSignUpForm, VolunteerSignUpForm, ActivityForm
from ..models import Staff, User, Activity
from django.db import transaction
from ..forms import *
from ..models import *

now = timezone.now()


class StaffSignUpView(CreateView):
    model = User
    form_class = StaffsSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'staffs'
        # Staff.objects.create(user=**kwargs)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return redirect('admins:signup')


class staff_home(ListView):
    model = Staff
    template_name = 'staff/staff.html'


def activity_list(request):
    # activity = Activity.objects.all()
    activity = Activity.objects.filter(created_date__lte=timezone.now())
    return render(request, 'staff/activity_list.html', {'activity': activity})


@login_required
def activity_edit(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == "POST":
        # update
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.updated_date = timezone.now()
            activity.save()
            activity = Activity.objects.filter(created_date__lte=timezone.now())
            return render(request, 'staff/activity_list.html',
                          {'activity': activity})
    else:
        # edit
        form = ActivityForm(instance=activity)
    return render(request, 'staff/activity_edit.html', {'form': form})


@login_required
def activity_delete(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    activity.delete()
    return redirect('staff:activity_list')


def activity_new(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ActivityForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            activity = form.save(commit=False)
            activity.created_date = timezone.now()
            activity.save()
            activity = Activity.objects.filter(created_date__lte=timezone.now())
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'staff/activity_list.html', {'activity': activity})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ActivityForm()

    return render(request, 'staff/activity_new.html', {'form': form})


def activity_detail(request, pk):
    model = Activity
    activity = get_object_or_404(Activity, pk=pk)
    context = {'activity': activity}
    return render(request, 'staff/activity_detail.html', {'activity': activity})


def activity_notes(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == "POST":
        # update
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.updated_date = timezone.now()
            activity.save()
            activity = Activity.objects.filter(created_date__lte=timezone.now())
            return render(request, 'staff/activity_notes.html',
                          {'activity': activity})
    else:
        # edit
        form = ActivityForm(instance=activity)
    return render(request, 'staff/activity_edit.html', {'form': form})