# 外部ライブラリ
from django.urls import path

# 独自ライブラリ
from snippets import views

urlpatterns = [
    path("snippets/", views.snippet_list),  # type: ignore
    path("snippets/<int:pk>/", views.snippet_detail),  # type: ignore
]
