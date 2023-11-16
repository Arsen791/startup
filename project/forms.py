from django import forms
from django.forms import Form
from .models import Comment, Blog
class RatingForm(forms.Form):
    RATING_CHOICES = (
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    )
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',] 

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'image'] 