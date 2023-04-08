# 外部ライブラリ
from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView

# 独自ライブラリ
from snippets.serializers import UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
