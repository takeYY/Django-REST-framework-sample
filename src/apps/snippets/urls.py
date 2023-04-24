# 外部ライブラリ
from django.urls import include, path
from rest_framework.routers import DefaultRouter

# 独自ライブラリ
from apps.snippets.views import SnippetViewSet, UserViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"snippets", SnippetViewSet, basename="snippet")
router.register(r"users", UserViewSet, basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
