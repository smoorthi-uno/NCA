from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('admins:signup')
        elif request.user.is_staffs:
            return redirect('staff:staff_home')
        else:
            return redirect('volunteer:volunteer_home')
    return render(request, 'nca/home.html')
