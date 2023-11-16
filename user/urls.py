from django.urls import path, include
from .views import login_page, register_page, logout_page, settings_page, login_course_creator


urlpatterns = [
    path('login/', login_page, name='login'),
	path('login_course_creator/', login_course_creator, name='login_course_creator'),
    path('register/', register_page, name='registration'),
    path('logout/', logout_page, name='logout'),
	path('settings/', settings_page, name='settings_page'),



]
