"""Views"""

# pylint: disable=E1101
from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from django.views.generic import View, ListView, DetailView
from .models import Post, Comment, Category


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
                "popular_post": [popular_post],
                "trending_posts": trending_posts,
                "editors_pick": [editors_pick],
            },
        )


class CategoryPage(ListView):
    """
    A view class for displaying a list of posts based on a specific category.

    """

    template_name = "category.html"
    paginate_by = 3
    model = Category
    context_object_name = "posts"

    def get_queryset(self, **kwargs):
        """
        Queries the posts related to a category from the database
        """
        # Get the slug parameter from the URL
        slug = self.kwargs["slug"]

        # Filter the queryset based on the slug
        category = get_object_or_404(Category, title=slug)
        queryset = Post.objects.filter(category=category, approved=True)

        print(queryset)

        return queryset


class PostDetailPage(DetailView):
    model = Post
    template_name = "post-detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.filter(approved=True).order_by(
            "-created_on"
        )
        context["commented"] = False
        context["liked"] = self.object.likes.filter(id=self.request.user.id).exists()
        context["popular_posts"] = self.get_popular_posts()
        popular_posts = self.get_popular_posts()

        print(f"popular posts = {popular_posts}")
        return context

    def get_popular_posts(self):
        return (
            Post.objects.filter(category=self.object.category, approved=True)
            .exclude(pk=self.object.id)
            .annotate(comment_count=Count("comments"))
        )
