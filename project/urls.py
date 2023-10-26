from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='home'),
    path('careers/', views.careers_page, name='careers'),
    path('project/<int:pk>/', views.course_details, name='course_details'),
    path('rate/<int:blog_id>/<int:rating>/', views.rate, name='rate'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
