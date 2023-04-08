# 外部ライブラリ
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# 独自ライブラリ
from snippets.views import SnippetDetail, SnippetList

urlpatterns = [
    path("snippets/", SnippetList.as_view()),
    path("snippets/<int:pk>/", SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
