# 独自ライブラリ
from apps.snippets.serializers import UserSerializer

# 外部ライブラリ
from django.contrib.auth.models import User
from rest_framework.viewsets import ReadOnlyModelViewSet


class UserViewSet(ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
