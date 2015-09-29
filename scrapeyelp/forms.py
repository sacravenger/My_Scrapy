from django import forms

from .models import Reviews, Urls

class PostForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ('username', 'rating','note', 'sourceid',)

class GetUrl(forms.ModelForm):

    class Meta:
        model = Urls
    	fields = ('url',)
        