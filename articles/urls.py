from django.urls import path
from .api import ArticleList, rate_article , ArticleRatingList

urlpatterns = [
    path('articles/', ArticleList.as_view(), name='article-list'),
    path('rate-article/', rate_article, name='rate-article'),
    path('rate-list/', ArticleRatingList.as_view(), name='rate-list'),
]
