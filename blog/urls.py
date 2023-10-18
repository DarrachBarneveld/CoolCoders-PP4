"""URL Patterns"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("<slug:slug>/", views.CategoryPage.as_view(), name="index"),
    path("post/<slug:slug>/", views.PostDetailPage.as_view(), name="post-detail"),
]
