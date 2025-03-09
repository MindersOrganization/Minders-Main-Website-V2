from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MagazineViewSet, VolumeViewSet, ArticleViewSet, ContributorViewSet, ArticleContributorViewSet

router = DefaultRouter()
router.register(r'magazines', MagazineViewSet)
router.register(r'volumes', VolumeViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'contributors', ContributorViewSet)
router.register(r'article_contributors', ArticleContributorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
