"""Views"""

# pylint: disable=E1101
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.views import generic
from .models import Post, Comment, Category
from .forms import (
    PostForm,
    UpdateUserForm,
    UpdateBioForm,
    CommentForm,
    CustomPasswordChangeForm
)


class HomePageView(generic.View):
    """
    A view class for displaying a list of categories and featured posts on the
    homepage.

    """

    def get(self, request):
        """
        Retrieves the posts from the database and returns the most popular,
        trending by likes and editors pick

        """
        all_posts = Post.objects.filter(approved=True)
        popular_post = (
            all_posts.annotate(comment_count=Count("comments"))
            .order_by("-comment_count")
            .first()
        )

        trending_posts = (
            all_posts.annotate(like_count=Count("likes"))
            .order_by("-like_count")[:3]
            )

        editors_pick = get_object_or_404(
            Post, slug="ais-influence-on-tech-shaping-the-future"
        )

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


class CategoryPage(generic.ListView):
    """
    A view class for displaying a list of posts based on a specific category.

    """

    template_name = "category.html"
    paginate_by = 6
    model = Category
    context_object_name = "posts"

    def get_queryset(self):
        """
        Queries the posts related to a category from the database
        """
        # Get the slug parameter from the URL
        slug = self.kwargs["slug"]

        # Filter the queryset based on the slug
        category = get_object_or_404(Category, title=slug)
        queryset = Post.objects.filter(category=category, approved=True)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs["slug"]
        category = get_object_or_404(Category, title=slug)

        context["category"] = category

        return context


class PostDetailPage(generic.View):
    """
    A view class for displaying the detail page of a blog post, including its
    comments, comment submission, and related posts.

    """

    template_name = "post-detail.html"

    def get_context_data(self, **kwargs):
        """
        Retrieve context data for rendering the post detail page.

        Args:
        - **kwargs: Additional keyword arguments passed to the view.

        Returns:
        - dict: A dictionary containing context data for rendering the page.
        """

        slug = kwargs.get("slug")
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(approved=True)
        context = {
            "post": post,
            "comments": comments.order_by("-created_on"),
            "comment_form": CommentForm(),
            "commented": False,
            "liked": post.likes.filter(id=self.request.user.id).exists(),
            "top_related_posts": self.get_top_related_posts(post),
        }
        return context

    def get_top_related_posts(self, post):
        """
        Get a list of top-related posts within the same category as the
        given post.

        Args:
        - post: The Post object for which to find related posts.

        Returns:
        - QuerySet: A queryset of related Post objects.
        """
        posts = (
            Post.objects.filter(category=post.category, approved=True)
            .exclude(pk=post.id)[:3]
            )
        return posts

    def get(self, request, slug):
        """
        Handle HTTP GET requests for rendering the post detail page.

        Args:
        - request: The HTTP request object.
        - slug: The slug of the requested post.
        - *args: Additional positional arguments.
        - **kwargs: Additional keyword arguments.

        Returns:
        - HttpResponse: Renders the post detail page with context data.
        """

        context = self.get_context_data(slug=slug)
        return render(request, self.template_name, context)

    def post(self, request, slug):
        """
        Handle HTTP POST requests for submitting a comment on the post.

        Args:
        - request: The HTTP request object.
        - slug: The slug of the post on which the comment is being submitted.

        Returns:
        - HttpResponse: Renders the post detail page with context data.
        """
        comment_form = CommentForm(data=request.POST)
        post = get_object_or_404(Post, slug=slug)
        context = self.get_context_data(slug=slug)

        if "delete_item" in request.POST:
            comment_id = request.POST.get("item_id")
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            messages.success(
                self.request,
                "Comment deleted successfully!")

        elif comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(
                self.request,
                "Comment created successfully! Review in progress!"
            )
        else:
            messages.error(
                self.request,
                "There was an error. Action not registered!")

        return render(request, self.template_name, context)


class PostLike(generic.View):
    """
    Handles the liking/unliking of a post.

    Methods:
    - post: Handles the POST request to like or unlike a post and redirects the
      user to the post's detail page.
    """

    def post(self, request, slug):
        """
        Handles the liking/unliking of a post and redirects to the post's
        detail page.
        """
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.error(
                self.request,
                "Post unliked successfully! Removed from your favourites!"
            )

        else:
            post.likes.add(request.user)
            messages.success(
                self.request,
                "Post liked successfully! Added to your favourites!"
            )

        return HttpResponseRedirect(reverse("post-detail", args=[slug]))


class AddPostPage(LoginRequiredMixin, generic.CreateView):
    """
    Allows a logged-in user to create a new blog post.

    Methods:
    - form_valid: Overrides the base method to set the post author to the
      currently logged-in user before saving the form.

    Mixins:
    - LoginRequiredMixin: Ensures that only authenticated users can access
      this view.
    """

    form_class = PostForm
    template_name = "add_post.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(
            self.request,
            "Post created successfully! Review in progress!")
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(
            self.request,
            "Post creation failed. Please check your input.")
        return response


class EditPostPage(LoginRequiredMixin, UserPassesTestMixin,
                   generic.UpdateView):
    """
    Allows a logged-in user to edit an existing blog post.

    - get_queryset: Filters the queryset to only include posts authored by
      the currently logged-in user.
    - dispatch: Overrides the base method to handle the case where the post
      is not found and returns a custom template response.
    - post: Handles HTTP POST requests, allowing the user to delete their post.
    - form_valid: Overrides the base method to set the post as unapproved after
      editing.
    - get_form_kwargs: Overrides the base method to provide the instance to the
      form.

    Mixins:
    - LoginRequiredMixin: Ensures that only authenticated users can access
      this view, and they must be the author of the post.
    """

    model = Post
    form_class = PostForm
    template_name = "edit_post.html"
    success_url = "/"

    def post(self, request, *args, **kwargs):
        # Check if the "delete_item" field is present in the POST data
        if "delete_item" in request.POST:
            post = self.get_object()
            if post:
                post.delete()
                messages.success(request, "Post deleted successfully.")
                return redirect("/")

            messages.error(
                request,
                "There was an error with your request, please try again."
            )

        return super().post(request, *args, **kwargs)

    def test_func(self):
        """
        UserPassesTestMixin function to prevent another user from updating
        other's post
        """

        post = self.get_object()
        return post.author == self.request.user

    def form_valid(self, form):
        """
        Handles a valid form submission and sets the post as unapproved.

        Returns:
        - HttpResponse: Redirects to the success URL after saving the post.
        """
        form.instance.approved = False
        messages.success(
            self.request,
            "Post edited successfully! Review in progress!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Post editing failed. Please check your input.")
        return super().form_invalid(form)


class ProfilePageView(generic.DetailView):
    """
    A view for displaying a user's profile page, including their posts,
    liked posts, and statistics.

    """

    template_name = "profile.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        """
        Retrieve the user object based on the provided username.

        """
        return get_object_or_404(User, username=self.kwargs.get("username"))

    def get_context_data(self, **kwargs):
        """
        Prepares and adds additional context data for rendering
        the profile page.

        Returns:
            dict: A dictionary containing the context data to be
            used in the template.
        """
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        posts_per_page = 4

        posts = Post.objects.filter(author=user, approved=True)
        total_posts = posts.count()

        # Filter by posts the user likes
        favourites = user.blogpost_like.filter(approved=True)

        # Generate total number of comments on authors posts
        total_comments = (
            Comment.objects.filter(post__in=posts, approved=True)
            .count()
            )

        # Generate total number of likes of all posts
        total_likes = sum(post.number_of_likes() for post in posts)

        posts_paginator = Paginator(posts, posts_per_page)
        favourites_paginator = Paginator(favourites, posts_per_page)

        posts_page_number = self.request.GET.get("posts_page")
        favourites_page_number = self.request.GET.get("favourites_page")

        posts_page = posts_paginator.get_page(posts_page_number)
        favourites_page = favourites_paginator.get_page(favourites_page_number)

        pending_posts = Post.objects.filter(author=user, approved=False)

        context["total_posts"] = total_posts
        context["total_comments"] = total_comments
        context["favourites"] = favourites
        context["total_likes"] = total_likes
        context["posts_page"] = posts_page
        context["favourites_page"] = favourites_page
        context["pending_posts"] = pending_posts


        return context


class UpdateProfileView(LoginRequiredMixin, generic.View):
    """
    Allows a user to update their profile information, including username,
    password, and bio.
    """

    template_name = "update_profile.html"
    user_form_class = UpdateUserForm
    password_form_class = CustomPasswordChangeForm
    bio_form_class = UpdateBioForm

    def get_context_data(self, **kwargs):
        """
        Retrieves context data for rendering the profile update page.
        Returns:
        - dict: A dictionary containing context data for rendering the page.
        """
        user = self.request.user
        context = {
            "user_form": kwargs.get("user_form",
                                    self.user_form_class(instance=user)),
            "password_form": kwargs.get(
                "password_form", self.password_form_class(user)
            ),
            "bio_form": kwargs.get(
                "bio_form", self.bio_form_class(instance=user.profile)
            ),
        }
        return context

    def get(self, request):
        """
        Handles HTTP GET requests for rendering the profile update page.

        Returns:
        - HttpResponse: Renders the profile update page with context data.
        """
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def process_form(self, request, form, form_name):
        """
        Process and handle form submission within a view.

        This method is responsible for processing a form
        submission within a view. It saves the form data if the form is valid,
        displays success or error messages, and updates the context
        to include the form for rendering in the template.


        """
        context = self.get_context_data()

        if form.is_valid():
            form.save()
            messages.success(self.request, f"{form_name} updated")
        else:
            messages.error(
                self.request, "Profile update failed, please check your input"
            )

        if form_name == "Biography":
            context["bio_form"] = form
        elif form_name == "Password":
            context["password_form"] = form
            update_session_auth_hash(self.request, self.request.user)
        elif form_name == "User details":
            context["user_form"] = form

        return render(request, self.template_name, context)

    def post(self, request):
        """
        Handle POST requests and form submissions within a view.

        This method is responsible for handling HTTP POST requests,
        including form submissions, within a view. It processes
        various forms (user_form, bio_form, password_form), displays
        appropriate success or error messages, and performs
        actions like updating user data or deleting the user's account.

        """
        context = self.get_context_data()

        user_form = self.user_form_class(
            request.POST,
            instance=request.user)
        bio_form = self.bio_form_class(
            request.POST,
            instance=request.user.profile)

        password_form = self.password_form_class(
            request.user,
            request.POST)

        if "bio_form" in request.POST:
            return self.process_form(request, bio_form, "Biography")

        if "password_form" in request.POST:
            return self.process_form(request, password_form, "Password")

        if "user_form" in request.POST:
            return self.process_form(request, user_form, "User details")

        # Delete user from database
        if "delete_item" in request.POST:
            try:
                user = request.user
                user.delete()
                messages.error(request, "Account Deleted.")
                return redirect("home")

            except Exception as e:  # pylint: disable=broad-except

                messages.error(
                    request,
                    f"There was an error deleting your account.{e}")

            return redirect("home")

        return render(request, self.template_name, context)
