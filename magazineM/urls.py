import os

from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.views.static import serve
from .views import (
    MagazineListCreateView, MagazineDetailView,
    VolumeListCreateView, VolumeDetailView,
    ArticleListCreateView, ArticleDetailView,
    ContributorListCreateView, ContributorDetailView,
    ArticleContributorListCreateView, ArticleContributorDetailView
)


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for Minders' magazine's backend",
        contact=openapi.Contact(email="minders.backend@gmail.com "),
    ),
    public=True,
    permission_classes=(permissions.IsAdminUser,), # to be edited after authentication isA
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
    # -------------------- Swagger --------------------
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger-static/<path:path>', serve, {'document_root': os.path.join(settings.STATIC_ROOT, 'swagger-ui-dist')}),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
