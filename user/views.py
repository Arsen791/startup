from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, Group
from django.contrib.auth import login
from .forms import UserRegistrationForm, LoginForm, ProfileForm, CourseCreatorLoginForm
import random
from .models import Profile



def login_page(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.data.get('username'), password=form.data.get('password'))
            try:
                profile = Profile.objects.get(owner_id=user.id)
            except:
                profile = Profile(owner_id=user.id)
                profile.save()
            login(request, user)
            if user is not None:
                return redirect('/')
            else:
                form.add_error(field='username', error='Invalid password or login')
                return render(request, 'user/login.html', {'form': form})
        else:
            return render(request, 'user/login.html', {'form': form})
        


def login_course_creator(request):
    if request.method == 'GET':
        form = CourseCreatorLoginForm()
        return render(request, 'user/coursecreatorlogin.html', {'form': form})
    if request.method == 'POST':
        form = CourseCreatorLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.data.get('username'), password=form.data.get('password'))
            try:
                profile = Profile.objects.get(owner_id=user.id)
            except:
                profile = Profile(owner_id=user.id)
                profile.save()
            login(request, user)
            if user is not None and user.groups.filter(name='Course Creators').exists():
                return redirect('/create_blogs')
            else:
                form.add_error(field='username', error='Invalid password or login')
                return render(request, 'user/coursecreatorlogin.html', {'form': form})
        else:
            return render(request, 'user/coursecreatorlogin.html', {'form': form})


def register_page(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'user/register.html', {'form': form})
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            profile = Profile(owner_id=user.id)
            profile.save()
            auth_data = auth.authenticate(request, email=user.email, password=form.data.get('password'))
            if auth_data is not None:
                login(request, auth_data)
                return redirect('/')
            return redirect('/auth/login/')
        else:
            return render(request, 'user/register.html', {'form': form})



def logout_page(request):
    auth.logout(request)
    return redirect('/auth/login')

def settings_page(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            profile = Profile.objects.get(owner_id=request.user.id)
            profile_form = ProfileForm(data={'bio': profile.bio}, files={'image': profile.image, 'resume': profile.resume})
            return render(request, 'user/profile.html', {'form': profile_form, 'profile': profile})
        if request.method == 'POST':
            profile_form = ProfileForm(request.POST, request.FILES)
            profile = Profile.objects.get(owner_id=request.user.id)
            if profile_form.is_valid():
                profile.bio = profile_form.data.get('bio')
                profile.image = profile_form.files.get('image')
                profile.resume = profile_form.files.get('resume')
                profile.save()
                return render(request, 'user/profile.html', {'form': profile_form, 'profile': profile})
            else:
                return render(request, 'user/profile.html', {'form': profile_form, 'profile': profile})
    else:
        return redirect('/')