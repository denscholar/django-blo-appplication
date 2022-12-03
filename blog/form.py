from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    name = forms.CharField(label='Hello', widget=forms.TextInput())
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
    

