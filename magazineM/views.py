from rest_framework import generics
from .models import Magazine, Volume, Article, Contributor, ArticleContributor
from .serializers import (
    MagazineSerializer, VolumeSerializer, ArticleSerializer,
    ContributorSerializer, ArticleContributorSerializer,
)

# -------------- Magazine --------------
class MagazineListCreateView(generics.ListCreateAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
class MagazineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer

# -------------- Volume --------------
class VolumeListCreateView(generics.ListCreateAPIView):
    serializer_class = VolumeSerializer
    def get_queryset(self):
        magazine_id = self.kwargs['magazine_id']
        return Volume.objects.filter(magazine_id=magazine_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['magazine_id'] = self.kwargs['magazine_id']
        return context

class VolumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VolumeSerializer

    def get_queryset(self):
        magazine_id = self.kwargs['magazine_id']
        return Volume.objects.filter(magazine_id=magazine_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['magazine_id'] = self.kwargs['magazine_id']
        return context

# -------------- Article --------------
class ArticleListCreateView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    def get_queryset(self):
        volume_id = self.kwargs['volume_id']
        return Article.objects.filter(volume_id=volume_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['volume_id'] = self.kwargs['volume_id']
        return context


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        volume_id = self.kwargs['volume_id']
        return Article.objects.filter(volume_id=volume_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['volume_id'] = self.kwargs['volume_id']
        return context

# -------------- Article Contributor --------------
class ArticleContributorListCreateView(generics.ListCreateAPIView):
    serializer_class = ArticleContributorSerializer
    def get_queryset(self):
        article_id = self.kwargs['article_id']
        return ArticleContributor.objects.filter(article_id=article_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['article_id'] = self.kwargs['article_id']
        return context


class ArticleContributorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleContributorSerializer
    def get_queryset(self):
        article_id = self.kwargs['article_id']
        return ArticleContributor.objects.filter(article_id=article_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['article_id'] = self.kwargs['article_id']
        context['contributor_id'] = self.request.data.get('contributor')  # Optional
        return context

# -------------- Contributor --------------
class ContributorListCreateView(generics.ListCreateAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

class ContributorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer