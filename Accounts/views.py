from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Register
from .models import Login
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import EmailAuthenticationForm
from .forms import CreateUserFormOwner, UserRegistrationForm
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core import mail
from django.conf import settings


from myproject.tokens import account_activation_token
from django.contrib.auth import get_user_model

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid!')
    
    return redirect('home')

def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()



            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('home')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="register.html",
        context={"form": form}
        )


from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(
        request=request,
        template_name="login.html", 
        context={'form': form}
    )



'''def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')

    context = {'form':form}
    return render(request, 'register.html', context)

def registerPageOwner(request):
    form = CreateUserFormOwner()

    if request.method == 'POST':
        form = CreateUserFormOwner(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')

    context = {'form':form}
    return render(request, 'register_owner.html', context)'''


'''def loginPage(request):
    form = EmailAuthenticationForm()

    if request.method == 'POST':
        form = EmailAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('')  
    else:
        form = EmailAuthenticationForm()

    context = {'form': form}
    return render(request, 'login.html', context)'''


'''def loginPage(request):
    form = EmailAuthenticationForm()

    if request.method == 'POST':
        form = EmailAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                # Handle authentication failure, for example, by adding an error message to the form
                form.add_error(None, 'Invalid email or password.')

    # If the request method is not POST or authentication fails, render the login page with the form
    context = {'form': form}
    return render(request, 'login.html', context)'''




