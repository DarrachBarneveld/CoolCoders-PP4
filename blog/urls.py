"""URL Patterns"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("<slug:slug>/", views.CategoryPage.as_view(), name="index"),
    path("add_post/", views.AddPostPage.as_view(), name="add_post"),
    path("post/<slug:slug>/", views.PostDetailPage.as_view(), name="post-detail"),
]
