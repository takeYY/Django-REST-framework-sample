# 外部ライブラリ
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView

# 独自ライブラリ
from snippets.serializers import UserSerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
