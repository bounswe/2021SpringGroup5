from django.shortcuts import render, redirect
from .models import User
from django.urls import reverse
import hashlib
from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import render_to_string
from .utils import generate_token
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout
from app import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError


def send_mail(user, request):
    current_site = get_current_site(request)
    mail_subject = 'Complete Your Login'
    mail_body = render_to_string('verification.html', {
        'User': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)

    })

    email = EmailMessage(subject=mail_subject, body=mail_body,
                         from_email=settings.EMAIL_HOST_USER,
                         to=[User.mail])
    email.send(fail_silently=False)


def register_first(request):
    if request.method == 'POST':

        context = {'has_error': False, 'data': request.POST}

        mail = request.POST.get('mail')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        if User.objects.filter(mail=mail).exists():
            messages.add_message(request, messages.ERROR,
                                 'Mail address is already taken, please choose another')
            return render(request, 'signup.html', status=409)

        user = User()
        user.name = name
        user.surname = surname
        user.mail = mail

        # send_mail(user1, request)
        context2 = {'user': user}
        return render(request, 'second_signup.html', context2)

    return render(request, 'signup.html')


def register_second(request):
    if request.method == 'POST':
        context = {'data': request.POST}
        username = request.POST.get('username')
        password = request.POST.get('passsword')
        password2 = request.POST.get('passsword2')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        mail = request.POST.get('mail')

        if password != password2:
            messages.add_message(request, messages.ERROR,
                                 'Passwords are not equal, please try again')
            return render(request, 'second_signup.html', context, status=401)

        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR,
                                 'Username is taken, choose another one')
            context['has_error'] = True

            return render(request, 'second_signup.html', context, status=409)

        user = User.objects.create_user(username=username, mail=mail, name=name, surname=surname)
        user.set_password(password)
        user.save()

        # if user and not user.is_email_verified:
        #      messages.add_message(request, messages.ERROR,
        #                         'Email is not verified, please check your email inbox')
        #     return render(request, 'second_signup.html', context, status=401)

        if not user:
            messages.add_message(request, messages.ERROR,
                                 'Invalid credentials, try again')
            return render(request, 'second_signup.html', context, status=401)

        login(request, user)

        messages.add_message(request, messages.SUCCESS,
                             f'Welcome {user.username}')
        return redirect(reverse('home'))

    return render(request, 'second_signup.html')


def logout_user(request):
    logout(request)

    messages.add_message(request, messages.SUCCESS,
                         'Successfully logged out')

    return redirect(reverse('login'))


def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             'Email verified, you can now login')
        return redirect(reverse('login'))

    return render(request, 'verification_failed.html', {"user": user})


def home(request):
    return render(request, 'home.html')
