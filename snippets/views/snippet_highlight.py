# 外部ライブラリ
from rest_framework import renderers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# 独自ライブラリ
from snippets.models import Snippet


class SnippetHighlight(GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
