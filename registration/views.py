from django.contrib.auth import logout
from django.shortcuts import render
from .forms import Custom_user_form
from django.urls import reverse_lazy
from django.views.generic import CreateView

def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')
class SignUp(CreateView):
    form_class = Custom_user_form
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'