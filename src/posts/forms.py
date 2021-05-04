from django import forms
from .models import Post,Comment


class PostModelForm(forms.ModelForm):
    content = forms.CharField(label="İçerik" ,widget=forms.Textarea(attrs={"rows":2}))

    class Meta:
        model = Post
        fields = ("content", "image",)

class CommentModelForm(forms.ModelForm):
    
    body = forms.CharField(label= "" ,max_length=250, widget= forms.TextInput(attrs={"placeholder":"bir yorum ekleyin."}))
    class Meta:
        model = Comment
        fields = ("body",)

