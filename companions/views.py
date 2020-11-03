from datetime import datetime
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse, Http404, QueryDict, HttpResponseRedirect
from django.db import IntegrityError
from django.contrib.auth import (authenticate, get_user_model, login, logout,)
from .forms import UserLogin, UserProfile
from .models import UserProfileModel, User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
# Create your views here.
    #home page
@login_required
def special_view(request):
    return HttpResponse("You have successfully logged in!")
@csrf_exempt
def home_view(request):  
    return render(request, "companions/index.html")
    #login view
@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("You were inactive")
        else:
            print("your login attempt has failed")
    else:
        return render(request, 'companions/components/login.html', {})
    #logout view
@csrf_exempt
@login_required
def logout_view(request):
    logout(request)
    title = "Logout"
    #redirects to home page
    return redirect("/")
    return render(request, "companions/form.html", {"title": title})
@login_required
def companions(request):
    return render(request, "companions/top10companions.html")
@login_required
def jannatulFirdous(request):
    return render(request, "companions/top6.html")
def register_view(request):
    register = False
    if request.method == 'POST':
        user_form = UserLogin(data=request.POST)
        profile = UserProfile(data=request.POST)
        if user_form.is_valid() and profile.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user_fprofule = profile.save(commit = False)
            user_fprofule = user
            if 'profile_picture' in request.FILES:
                print("YES")
                user_fprofule.profile_picture = request.FILES['profile_picture']
            user_fprofule.save()
            register = True
        else:
            print(user_form.errors, profile.errors)
    else:
        user_form = UserLogin()
        profile = UserProfile()
    return render(request, 'companions/components/register.html', {'user_form': user_form, 'profile':profile, 'registered':register})
def first_companion(request):
    return render(request, 'companions/AbuBakr.html')
def second_companion(request):
    return render(request, 'companions/Umar.html')
def third_companion(request):
    return render(request, 'companions/Uthman.html')
def fourth_companion(request):
    return render(request, 'companions/Ali.html')
def fifth_companion(request):
    return render(request, 'companions/Talhah.html')
def sixth_companion(request):
    return render(request, 'companions/Zubayr.html')
def seventh_companion(request):
    return render(request, 'companions/AbdurRahman.html')
def eighth_companion(request):
    return render(request, 'companions/Saad.html')
def ninth_companion(request):
    return render(request, 'companions/Said.html')
def tenth_companion(request):
    return render(request, 'companions/AbuUbaidah.html') 