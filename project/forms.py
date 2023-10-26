from django import forms
class RatingForm(forms.Form):
    RATING_CHOICES = (
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    )
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)