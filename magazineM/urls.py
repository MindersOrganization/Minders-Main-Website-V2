from django.urls import path
from .views import (
    MagazineListCreateView, MagazineDetailView,
    VolumeListCreateView, VolumeDetailView,
    ArticleListCreateView, ArticleDetailView,
    ContributorListCreateView, ContributorDetailView,
    ArticleContributorListCreateView, ArticleContributorDetailView
)

urlpatterns = [
    # -------------------- Magazine --------------------
    path('magazines/', MagazineListCreateView.as_view(), name='magazine-list-create'),  # List all or create a new one
    path('magazines/<int:pk>/', MagazineDetailView.as_view(), name='magazine-detail'),  # Retrieve, update, or delete
    # -------------------- Volume --------------------
    path('magazines/<int:magazine_id>/volumes/', VolumeListCreateView.as_view(), name='volume-list-create'),
    path('magazines/<int:magazine_id>/volumes/<int:pk>/', VolumeDetailView.as_view(), name='volume-detail'),
    # -------------------- Article --------------------
    path('magazines/<int:magazine_id>/volumes/<int:volume_id>/articles/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('magazines/<int:magazine_id>/volumes/<int:volume_id>/articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    # -------------------- Article Contributors --------------------
    path('magazines/<int:magazine_id>/volumes/<int:volume_id>/articles/<int:article_id>/contributors/', ArticleContributorListCreateView.as_view(), name='article-contributor-list-create'),
    path('magazines/<int:magazine_id>/volumes/<int:volume_id>/articles/<int:article_id>/contributors/<int:pk>/', ArticleContributorDetailView.as_view(), name='article-contributor-detail'),
    # -------------------- Contributors --------------------
    path('contributors/', ContributorListCreateView.as_view(), name='contributor-list-create'),
    path('contributors/<int:pk>/', ContributorDetailView.as_view(), name='contributor-detail'),
]
