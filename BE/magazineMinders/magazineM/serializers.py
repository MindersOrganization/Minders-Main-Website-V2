from rest_framework import serializers
from .models import Magazine, Volume, Article, Contributor, ArticleContributor

class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'

class VolumeSerializer(serializers.ModelSerializer):
    magazine = MagazineSerializer()
    class Meta:
        model = Volume
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    volume = VolumeSerializer()
    class Meta:
        model = Article
        fields = '__all__'

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'

class ArticleContributorSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    contributor = ContributorSerializer()
    class Meta:
        model = ArticleContributor
        fields = '__all__'
