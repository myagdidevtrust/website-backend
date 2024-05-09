from django.urls import path
from . import views

urlpatterns = [
    path("news/", views.NewsListCreate.as_view(), name='news-list-create')
]