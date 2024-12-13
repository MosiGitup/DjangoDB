from django.shortcuts import render, redirect
from django.core.mail import send_mail


# def home(request):
#     language = request.POST.get('language')
#     request.session['language'] = language
#     first = request.POST.get('first')
#     client = Profile.objects.all()
#     return render(request, "home.html", {"first": first})


# def login(request):
#     language = request.session['language']
#     return render(request, "sign_in.html", {})
