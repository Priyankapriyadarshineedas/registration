from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.views import View

from .middlewares import guest, auth
from .models import CustomUser

# Create your views here.

from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Extract the data from the form
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            gender = form.cleaned_data['gender']
            image = form.cleaned_data['image']
            password = form.cleaned_data['password']

            # Create the user object
            user = CustomUser.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                gender=gender,
                image=image,
                password=password,
            )
            user.save()
            # Redirect to login page after successful registration
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'app/register.html', {'form': form})


@guest
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a dashboard or profile page after successful login
                return redirect('dashboard')
            else:
                form.add_error(None, 'Invalid email or password')  # Add non-field error
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})


@auth
def dashboard_view(request):
    return render(request, 'app/dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# Create your views here.
class SuccessPageView(View):
    def get(self, request):
        return render(request, 'app/successpage.html')


from django.shortcuts import render

# Create your views here.
