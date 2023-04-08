# 外部ライブラリ
from rest_framework.generics import ListCreateAPIView

# 独自ライブラリ
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
