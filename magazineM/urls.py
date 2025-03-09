from django.urls import path
from .views import (
    MagazineListCreateView, MagazineDetailView,
    VolumeListCreateView, VolumeDetailView,
    ArticleListCreateView, ArticleDetailView,
    ContributorListCreateView, ContributorDetailView,
    ArticleContributorListCreateView, ArticleContributorDetailView
)

urlpatterns = [
    # Magazine URLs
    path('magazines/', MagazineListCreateView.as_view(), name='magazine-list-create'),
    path('magazines/<int:pk>/', MagazineDetailView.as_view(), name='magazine-detail'),

    # Volume URLs (Inside a Magazine)
    path('magazines/<int:magazine_id>/volumes/', VolumeListCreateView.as_view(), name='volume-list-create'),
    path('magazines/<int:magazine_id>/volumes/<int:pk>/', VolumeDetailView.as_view(), name='volume-detail'),

    # Article URLs (Inside a Volume)
    path('magazines/<int:magazine_id>/volumes/<int:volume_id>/articles/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('magazines/<int:magazine_id>/volumes/<int:volume_id>/articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),

    # Article Contributor URLs (Inside an Article)
    path('magazines/<int:magazine_id>/volumes/<int:volume_id>/articles/<int:article_id>/contributors/', ArticleContributorListCreateView.as_view(), name='article-contributor-list-create'),
    path('magazines/<int:magazine_id>/volumes/<int:volume_id>/article-contributors/<int:pk>/', ArticleContributorDetailView.as_view(), name='article-contributor-detail'),

    # Contributor URLs
    path('contributors/', ContributorListCreateView.as_view(), name='contributor-list-create'),
    path('contributors/<int:pk>/', ContributorDetailView.as_view(), name='contributor-detail'),
]
