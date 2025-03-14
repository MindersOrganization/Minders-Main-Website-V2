from drf_yasg.openapi import Response
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from .models import Magazine, Volume, Article, Contributor, ArticleContributor
from .serializers import (
    MagazineSerializer, VolumeSerializer, ArticleSerializer,
    ContributorSerializer, ArticleContributorSerializer,
)

# ------------------ Magazine Views ------------------
class MagazineListCreateView(generics.ListCreateAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of all magazines.",
        responses={200: MagazineSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new magazine.",
        request_body=MagazineSerializer,
        responses={201: MagazineSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class MagazineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer

# ------------------ Volume Views ------------------
class VolumeListCreateView(generics.ListCreateAPIView):
    serializer_class = VolumeSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of all volumes for a specific magazine.",
        responses={200: VolumeSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new volume for a magazine.",
        request_body=VolumeSerializer,
        responses={201: VolumeSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

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

# ------------------ Article Views ------------------
class ArticleListCreateView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of all articles for a specific volume.",
        responses={200: ArticleSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new article for a volume.",
        request_body=ArticleSerializer,
        responses={201: ArticleSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

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

# ------------------ Article Contributor Views ------------------
class ArticleContributorListCreateView(generics.ListCreateAPIView):
    serializer_class = ArticleContributorSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of contributors for a specific article.",
        responses={200: ArticleContributorSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Add a contributor to an article.",
        request_body=ArticleContributorSerializer,
        responses={201: ArticleContributorSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

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
        return context

# ------------------ Contributor Views ------------------
class ContributorListCreateView(generics.ListCreateAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


class ContributorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
