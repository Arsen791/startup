"""
URL configuration for startup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from allauth.account import views as account_views
from allauth.socialaccount import views as socialaccount_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user.urls')),
    path('', include('project.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/social/login/cancelled/', socialaccount_views.LoginCancelledView.as_view(), name='socialaccount_login_cancelled'),
    path('accounts/social/login/error/', socialaccount_views.LoginErrorView.as_view(), name='socialaccount_login_error'),
]
