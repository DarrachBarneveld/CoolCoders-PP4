"""Views"""

# pylint: disable=E1101
from django.shortcuts import render
from django.views import View
from .models import Post


# Create your views here.
class HomePageView(View):
    """
    A view class for displaying a list of categories and featured posts on the homepage.

    """

    def get(self, request, *args, **kwargs):
        """
        Retrieves the posts from the database and returns the most popular, trending by likes
        and editors pick

        """
        all_posts = Post.objects.filter(approved=True)
        print(all_posts)

        return render(
            request,
            "home.html",
            {
                "all_posts": all_posts,
            },
        )
