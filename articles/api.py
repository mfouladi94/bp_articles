from django.db.models import Avg
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article, ArticleRating
from .serializers import ArticleSerializer, ArticleRatingSerializer, InputArticleRatingSerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleRatingList(generics.ListAPIView):
    queryset = ArticleRating.objects.all()
    serializer_class = ArticleRatingSerializer


@api_view(['POST'])
def rate_article(request):
    user = request.user
    input_serializer = InputArticleRatingSerializer(data=request.data)

    if not input_serializer.is_valid():
        return Response({"message": input_serializer.errors}, status=400)

    article_id = input_serializer.validated_data.get('article_id')
    rating = input_serializer.validated_data.get('rating')

    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        return Response({"message": "Article not found"}, status=404)

    rating_instance, created = ArticleRating.objects.get_or_create(user=user, article=article)
    rating_instance.rating = rating
    rating_instance.save()

    if created :
        article.rate_count += 1

    average_rating = ArticleRating.objects.filter(article_id=article_id).aggregate(avg_rating=Avg('rating'))
    average_rating_value = average_rating['avg_rating']
    article.rate_avg = average_rating_value
    article.save()

    return Response({"message": "Rating saved successfully"}, status=201)
