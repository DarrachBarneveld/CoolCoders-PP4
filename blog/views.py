"""Views"""

# pylint: disable=E1101
from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from django.views.generic import View
from .models import Post, Comment


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
        popular_post = (
            all_posts.annotate(comment_count=Count("comments"))
            .order_by("-comment_count")
            .first()
        )

        popular_post.comment_count = Comment.objects.filter(
            post=popular_post, approved=True
        ).count()

        trending_posts = all_posts.annotate(like_count=Count("likes")).order_by(
            "-like_count"
        )[:3]

        editors_pick = get_object_or_404(
            Post, slug="ais-influence-on-tech-shaping-the-future"
        )

        editors_pick.comment_count = Comment.objects.filter(
            post=editors_pick, approved=True
        ).count()

        return render(
            request,
            "home.html",
            {
                "all_posts": all_posts,
                "popular_post": popular_post,
                "trending_posts": trending_posts,
                "editors_pick": editors_pick,
            },
        )
