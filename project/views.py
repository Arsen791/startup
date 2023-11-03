from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Rating, Comment
from .forms import RatingForm, CommentForm
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

