from rest_framework import serializers
from .models import Magazine, Volume, Article, Contributor, ArticleContributor

class MagazineSerializer(serializers.ModelSerializer):
    """Serializer for Magazine model."""

    class Meta:
        model = Magazine
        fields = '__all__'


class VolumeSerializer(serializers.ModelSerializer):
    """Serializer for Volume model."""
    magazine = serializers.PrimaryKeyRelatedField(
        read_only=True, help_text="The ID of the associated magazine."
    )

    class Meta:
        model = Volume
        fields = ['id', 'title', 'magazine']

    def create(self, validated_data):
        magazine_id = self.context['magazine_id']
        validated_data['magazine'] = Magazine.objects.get(pk=magazine_id)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        magazine_id = self.context.get('magazine_id')
        if magazine_id:
            validated_data['magazine'] = Magazine.objects.get(pk=magazine_id)
        return super().update(instance, validated_data)


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer for Article model."""
    volume = serializers.PrimaryKeyRelatedField(
        read_only=True, help_text="The ID of the associated volume."
    )

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'volume']

    def create(self, validated_data):
        volume_id = self.context['volume_id']
        validated_data['volume'] = Volume.objects.get(pk=volume_id)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        volume_id = self.context.get('volume_id')
        if volume_id:
            validated_data['volume'] = Volume.objects.get(pk=volume_id)
        return super().update(instance, validated_data)


class ContributorSerializer(serializers.ModelSerializer):
    """Serializer for Contributor model."""

    class Meta:
        model = Contributor
        fields = '__all__'


class ArticleContributorSerializer(serializers.ModelSerializer):
    """Serializer for ArticleContributor model."""
    article_title = serializers.SerializerMethodField(help_text="Title of the related article.")
    contributor_name = serializers.SerializerMethodField(help_text="Name of the related contributor.")

    class Meta:
        model = ArticleContributor
        fields = ['id', 'article', 'article_title', 'contributor', 'contributor_name', 'role']
        extra_kwargs = {
            'article': {'read_only': True}
        }

    def get_article_title(self, obj):
        return obj.article.title

    def get_contributor_name(self, obj):
        return obj.contributor.name

    def create(self, validated_data):
        article_id = self.context.get('article_id')
        if not article_id:
            raise serializers.ValidationError({"article": "Article ID is missing in the URL."})

        contributor_id = self.initial_data.get('contributor')
        if not contributor_id:
            raise serializers.ValidationError({"contributor": "Contributor ID is required in the request body."})

        article = Article.objects.get(pk=article_id)
        contributor = Contributor.objects.get(pk=contributor_id)
        validated_data['article'] = article
        validated_data['contributor'] = contributor

        return super().create(validated_data)
