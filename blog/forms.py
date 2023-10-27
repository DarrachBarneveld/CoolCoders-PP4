"""Forms"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django_summernote.widgets import SummernoteWidget
from .models import Post, Profile, Comment


class PostForm(forms.ModelForm):
    """
    A form for creating  blog post instances.

    """

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["excerpt"].widget = forms.Textarea(attrs={"rows": 3})

    class Meta:
        """Get post model, choose fields to display"""

        model = Post
        fields = ["title", "category", "excerpt", "content", "featured_image"]
        widgets = {"content": SummernoteWidget()}


class UpdateUserForm(UserChangeForm):
    """
    A form for editing user information.

    """

    password = None

    class Meta:
        """Get User model, choose fields to display"""

        model = User
        fields = ["username", "email", "first_name", "last_name"]
        help_texts = {"username": None}


class UpdateBioForm(forms.ModelForm):
    """
    A form for editing user biography information.

    """

    class Meta:
        """Get Profile model, choose fields to display"""

        model = Profile
        fields = ["bio"]
        widgets = {
            "bio": forms.TextInput(),
        }


class CommentForm(forms.ModelForm):
    """
    A form for creating comments on blog posts.

    """

    class Meta:
        """Get Comment model, choose fields to display"""

        model = Comment
        fields = ("body",)