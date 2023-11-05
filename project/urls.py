from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from allauth.socialaccount import views as socialaccount_views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('careers/', views.careers_page, name='careers'),
    path('project/<int:pk>/', views.course_details, name='course_details'),
    path('rate/<int:blog_id>/<int:rating>/', views.rate, name='rate'),
    path('accounts/', include('allauth.urls')),
    path('accounts/social/login/cancelled/', socialaccount_views.LoginCancelledView.as_view(), name='socialaccount_login_cancelled'),
    path('accounts/social/login/error/', socialaccount_views.LoginErrorView.as_view(), name='socialaccount_login_error'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
