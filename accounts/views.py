from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib.auth import authenticate

from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.


class UserLogin(LoginView):
    form_class = UserLoginForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'


class UserSignUp(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             # Create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # Set the chosen password
#             new_user.set_password(user_form.cleaned_data['password1'])
#             # Save the User object
#             new_user.save()
#             return redirect('login')
#         else:
#             print(user_form.errors)
#             return render(request, 'accounts/signup.html', {'form': user_form})
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'accounts/signup.html', {'form': user_form})


