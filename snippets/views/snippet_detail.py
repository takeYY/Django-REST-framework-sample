# 外部ライブラリ
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# 独自ライブラリ
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
