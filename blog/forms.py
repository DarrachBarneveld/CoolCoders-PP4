"""Forms"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
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

    def clean_email(self):
        email = self.cleaned_data["email"]

        if (self.instance.email != email and
        User.objects.filter(email=email).exists()
        and email !=''):

            raise forms.ValidationError("A user with this email already exists!")

        return email



class UpdateBioForm(forms.ModelForm):
    """
    A form for editing user biography information.

    """

    class Meta:
        """Get Profile model, choose fields to display"""

        model = Profile
        fields = ["bio"]
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4})
             }


class CommentForm(forms.ModelForm):
    """
    A form for creating comments on blog posts.

    """

    class Meta:
        """Get Comment model, choose fields to display"""

        model = Comment
        fields = ("body",)


class CustomPasswordChangeForm(PasswordChangeForm):
    """
    A customized form for changing a user's password.

    This form inherits from Django's built-in PasswordChangeForm and provides
    some custom modifications:

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove autofocus attribute from the old password field
        self.fields["old_password"].widget.attrs.pop("autofocus", None)

        # Remove autofocus attribute from the new password1 field
        self.fields["new_password1"].widget.attrs.pop("autofocus", None)

        # Remove autofocus attribute from the new password2 field
        self.fields["new_password2"].widget.attrs.pop("autofocus", None)
