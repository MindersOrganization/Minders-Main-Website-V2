from rest_framework import serializers
from .models import Magazine, Volume, Article, Contributor, ArticleContributor


class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'


class VolumeSerializer(serializers.ModelSerializer):
    magazine = serializers.PrimaryKeyRelatedField(queryset=Magazine.objects.all(), write_only=True)

    class Meta:
        model = Volume
        fields = ['id', 'title', 'magazine']


class ArticleSerializer(serializers.ModelSerializer):
    volume = serializers.PrimaryKeyRelatedField(queryset=Volume.objects.all(), write_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'volume']


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'


class ArticleContributorSerializer(serializers.ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all(), write_only=True)
    contributor = serializers.PrimaryKeyRelatedField(queryset=Contributor.objects.all(), write_only=True)

    class Meta:
        model = ArticleContributor
        fields = ['id', 'article', 'contributor', 'role']
