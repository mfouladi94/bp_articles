from rest_framework import serializers
from .models import Article, ArticleRating


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleRating
        fields = '__all__'


class InputArticleRatingSerializer(serializers.Serializer):
    article_id = serializers.IntegerField(required=True)
    rating = serializers.IntegerField(required=True , min_value=0 , max_value=5)