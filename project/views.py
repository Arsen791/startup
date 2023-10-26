from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Rating
from .forms import RatingForm
from django.http import JsonResponse

def home_page(request):
    return render(request, 'project/index.html')


def careers_page(request ):
    courses = Blog.objects.all()
    return render(request, 'project/careers.html', {'courses': courses})

def course_details(request, pk):
    blogs = Blog.objects.get(pk=pk)
    blogs.increment_views() 
    average_rating = blogs.average_rating()
    user_rating = None
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(blog=blogs, user=request.user).first()

    return render(request, 'project/course_details.html', {'blogs': blogs, 'average_rating': average_rating, 'user_rating': user_rating})

def rate(request, blog_id, rating):
    blog = Blog.objects.get(pk=blog_id)
    Rating.objects.filter(blog=blog, user=request.user).delete()
    blog.rating_set.create(user=request.user, rating=rating)
    # Верните успешный HTTP-ответ, например, JSON-объект с сообщением об успешной операции
    return JsonResponse({'message': 'Rating updated successfully'})

    
