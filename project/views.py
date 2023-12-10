from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Rating, Comment, Notification
from .forms import RatingForm, CommentForm, BlogForm
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User



def create_blogs(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = BlogForm()
            return render(request, 'project/create_blogs.html', {'form': form})
        if request.method == 'POST':
            form = BlogForm(request.POST ,request.FILES)
            if form.is_valid():
                title = form.data.get('title')
                description = form.data.get('description')
                image = form.files.get('image')
                blogs = Blog(title=title, description=description, image=image, owner_id=request.user.id)
                blogs.save()
                message = f'Новый курс "{blogs.title}" доступен для обучения'
                notification = Notification.objects.create(message=message)
                notification.users.set(User.objects.all())
                return redirect('/create_blogs')
            else:
                return render(request, 'project/create_blogs.html', {'form': form})
    else:
        return redirect('/auth/login/')



def notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'project/notifications.html', {'notifications': notifications})

from django.http import HttpResponseServerError

def mark_notification_as_read(request, notification_id):
    if request.method == 'POST':
        try:
            notification = Notification.objects.get(pk=notification_id)
            notification.is_read = True
            notification.save()
            return redirect('/notifications')
        except Notification.DoesNotExist:
            return HttpResponseServerError('Notification does not exist')
        except Exception as e:
            return HttpResponseServerError(f'An error occurred: {e}')
 


def home_page(request):
    if request.user.is_authenticated:
        unread_notifications = Notification.objects.filter(users=request.user, is_read=False).count()
    else:
        unread_notifications = 0  # Задайте значение по умолчанию для анонимных пользователей

    return render(request, 'project/index.html', {'new_notifications_count': unread_notifications})


def careers_page(request ):
    courses = Blog.objects.all()
    unread_notifications = Notification.objects.filter(users=request.user, is_read=False).count()
    return render(request, 'project/careers.html', {'courses': courses,'new_notifications_count': unread_notifications})

def course_details(request, pk):
    blogs = Blog.objects.get(pk=pk)
    blogs.increment_views() 
    average_rating = blogs.average_rating()
    user_rating = None
    comments = Comment.objects.filter(blog=blogs, active=True, parent_comment=None)
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(blog=blogs, user=request.user).first()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.blog = blogs
            new_comment.save()
            comment_form = CommentForm()
            return redirect('course_details', pk=pk)  # Очистить форму после успешного сохранения комментария
    else:
        comment_form = CommentForm()

    return render(request, 'project/course_details.html', {'blogs': blogs, 'average_rating': average_rating, 'user_rating': user_rating, 'comment_form': comment_form,'comments': comments})

def rate(request, blog_id, rating):
    blog = Blog.objects.get(pk=blog_id)
    Rating.objects.filter(blog=blog, user=request.user).delete()
    blog.rating_set.create(user=request.user, rating=rating)
    # Верните успешный HTTP-ответ, например, JSON-объект с сообщением об успешной операции
    return JsonResponse({'message': 'Rating updated successfully'})

