from django.urls import path, include
from .views import login_page, register_page, logout_page
from allauth.socialaccount import views as socialaccount_views

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='registration'),
    path('logout/', logout_page, name='logout'),
	path('accounts/', include('allauth.urls')),
    path('accounts/social/login/cancelled/', socialaccount_views.LoginCancelledView.as_view(), name='socialaccount_login_cancelled'),
    path('accounts/social/login/error/', socialaccount_views.LoginErrorView.as_view(), name='socialaccount_login_error'),



]
