from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("review_query", views.review_query, name="review_query"),
]
