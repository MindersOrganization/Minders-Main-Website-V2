from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound
from .models import Magazine, Volume, Article, Contributor, ArticleContributor
from .serializers import MagazineSerializer, VolumeSerializer, ArticleSerializer, ContributorSerializer, ArticleContributorSerializer


# ---------------- Magazine Views ----------------
class MagazineListCreateView(generics.ListCreateAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    permission_classes = [AllowAny]


class MagazineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    permission_classes = [AllowAny]


# ---------------- Volume Views ----------------
class VolumeListCreateView(generics.ListCreateAPIView):
    serializer_class = VolumeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        magazine_id = self.kwargs['magazine_id']
        return Volume.objects.filter(magazine_id=magazine_id)

    def post(self, request, magazine_id):
        try:
            magazine = Magazine.objects.get(id=magazine_id)
        except Magazine.DoesNotExist:
            raise NotFound("Magazine not found.")

        data = request.data.copy()
        data["magazine"] = magazine.id
        serializer = VolumeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VolumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    permission_classes = [AllowAny]


# ---------------- Article Views ----------------
class ArticleListCreateView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        volume_id = self.kwargs['volume_id']
        return Article.objects.filter(volume_id=volume_id)

    def post(self, request, volume_id):
        try:
            volume = Volume.objects.get(id=volume_id)
        except Volume.DoesNotExist:
            raise NotFound("Volume not found.")

        data = request.data.copy()
        data["volume"] = volume.id
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]


# ---------------- Contributor Views ----------------
class ContributorListCreateView(generics.ListCreateAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [AllowAny]


class ContributorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [AllowAny]


# ---------------- Article Contributor Views ----------------
class ArticleContributorListCreateView(generics.ListCreateAPIView):
    serializer_class = ArticleContributorSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        article_id = self.kwargs['article_id']
        return ArticleContributor.objects.filter(article_id=article_id)

    def post(self, request, article_id):
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            raise NotFound("Article not found.")

        data = request.data.copy()
        data["article"] = article.id
        serializer = ArticleContributorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleContributorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArticleContributor.objects.all()
    serializer_class = ArticleContributorSerializer
    permission_classes = [AllowAny]
