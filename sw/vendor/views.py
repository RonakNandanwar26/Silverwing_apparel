from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Vendor
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def register(request):
    print('before post')
    if request.method == 'POST':
        print('Entered in post')
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        print(name)
        print(email)
        print(password)
        print('before if')
        if (password == confirm_password):
            print('entered')
            usr = User.objects.create_user(name,email,password)
            usr.is_active = False
            usr.save()
            request.session['vendor_email'] = email
            request.session['vendor_name'] = name
            reg = Vendor(user=usr)
            reg.save()
            subject = 'Hello ' + name + ' from apparel_vendor!'
            message = "Hello, " + name + ". Welcome To apparel. Please Verify Your Email ID ::--> " "http://127.0.0.1:8000/vendor/confirm_email/"
            email_from = settings.EMAIL_HOST_USER
            email_to = [email, ]
            send_mail(subject, message, email_from, email_to)
            return redirect('Vendor:please_verify')
        else:
            messages.error(request,'{}, Password and confirm password must be same...'.format(name))
    template = 'vendor/signup.html'
    return render(request,template)


def please_verify(request):
    return render(request,'vendor/verification_sent.html')

def confirm_email(request):
    template = 'vendor/confirm_email.html'
    email = request.session.get("vendor_email")
    usr = User.objects.get(email=email)
    usr.is_active = True
    usr.is_staff = True
    usr.save()

    vendor = {'name':usr.username, 'email': usr.email}
    request.session['vendor'] = vendor
    if (usr.is_staff == True):
        request.session.get('vendor')
        return redirect('Vendor:home')

    return render(request,template)


def home(request):
    return render(request,'vendor/index.html')




def login(request):
    print('before post')
    if request.method == 'POST':
        print('after post')
        user = request.POST['username']
        pwd = request.POST['password']

        usr = authenticate(username=user,password=pwd)
        print(usr)
        if usr:
            usr = User.objects.get(username=user)
            print('checking staff status')
            if (usr.is_staff == True):
                print('staff status true')
                print(usr)
                vendor = {'vendor_name':usr.username,'vendor_email':usr.email}
                request.session['vendor'] = vendor
                request.session['vendor_email'] = usr.email
                return redirect('Vendor:home')
            else:
                print('staff status false')
                messages.error(request,'You have no vendor account...')
                return render(request,'account/login.html')

    return render(request,'vendor/login.html')