from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from .models import Profile
from .forms import ProfileForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail


def home(request):
    language = request.POST.get('language')
    request.session['language'] = language
    return render(request, "home.html", {})


def login_page(request):
    language = request.POST.get('language')
    request.session['language'] = language
    first = request.POST.get('first')
    client = Profile.objects.all()
    suser = User.objects.all()
    suser_name = suser.values('username')
    UserName = client.values('Username')
    UserPass = client.values('Password')
    CL_domain = client.values('Domain')
    user_name = request.POST.get('user_name')
    request.session['user_name'] = user_name
    user_pass = request.POST.get('user_pass')
    request.session['user_pass'] = user_pass
    superusers = auth.authenticate(username=user_name, password=user_pass)
    first = request.POST.get('first')
    request.session['first'] = first
    if superusers is not None and superusers.is_active:
        auth.login(request, superusers)
        for i in range(len(suser_name)):
            if str(superusers) == suser_name[i]['username']:
                SuperUser = suser_name[i]['username']
                request.session['SuperUser'] = SuperUser
                client_domain = None
                request.session['client_domain'] = client_domain
        return render(request, "home.html", {"first": first, "admin_user": superusers, "lan": language})
    for i in range(len(UserName)):
        if UserName[i]['Username'] == user_name and UserPass[i]['Password'] == user_pass:
            client_domain = CL_domain[i]['Domain']
            request.session['client_domain'] = client_domain
            SuperUser = None
            request.session['SuperUser'] = SuperUser
            return render(request, "home.html", {"first": first, "client": user_name, "lan": language, "client_domain": client_domain})
    if first:
        return render(request, "sign_in.html", {"lan": language})
    else:
        return render(request, "sign_in.html", {"lan": language})


def logout_page(request):
    auth.logout(request)
    language = 'EN'
    if language == 'FR':
        return render(request, "sign_in_fr.html", {"lan": language})
    else:
        request.session['language'] = language
        return render(request, "sign_in.html", {"lan": language})


def register_page(request):
    submitted = False
    language = request.session['language']
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            First_name = form.cleaned_data['First_name']
            Last_name = form.cleaned_data['Last_name']
            Email = form.cleaned_data['Email']
            Domain = form.cleaned_data['Domain']
            request.session['First_name'] = First_name
            request.session['Last_name'] = Last_name
            request.session['Email'] = Email
            request.session['Domain'] = Domain
        if language == 'FR':
            return render(request, "sign_up_fr.html", {"reg_user": user, "f_name": First_name, "lan": language})
        else:
            return render(request, "sign_up.html", {"reg_user": user, "f_name": First_name, "lan": language})
    else:
        form = ProfileForm
        if 'submitted' in request.GET:
            submitted = True
    if language == 'FR':
        return render(request, "sign_up_fr.html", {"form": form, 'submitted': submitted, "lan": language})
    else:
        return render(request, "sign_up.html", {"form": form, 'submitted': submitted, "lan": language})


def contact(request):
    language = request.session['language']
    form = ProfileForm(request.POST)
    First_name = request.session['First_name']
    Last_name = request.session['Last_name']
    Email = request.session['Email']
    Domain = request.session['Domain']
    print(First_name + ' ' + Last_name)
    print(Email)
    print(Domain)
    # send_mail(
    #     First_name + Last_name,
    #     'He/She wants to register in website. His/Her interested project is ' + Domain,
    #     Email,
    #     ['mfeizabadi@dromadaire-geo.com'],
    #     )
    if language == 'FR':
        return render(request, "home_fr.html", {"lan": language})
    else:
        return render(request, "home.html", {"lan": language})


def forget_pass(request):
    language = request.session['language']
    email = request.POST.get('user_email')
    # send_mail(
    #     'Forgot password',
    #     email + ' user forgot the password.',
    #     email,
    #     ['mfeizabadi@dromadaire-geo.com'],
    #     )
    return render(request, "forget_pass.html", {"lan": language, "email": email})