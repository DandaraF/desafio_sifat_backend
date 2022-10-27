from core.models import Postagem
from rest_framework.viewsets import ModelViewSet

from .serializers import PostagemSerializer


class PostagemViewSet(ModelViewSet):
  queryset = Postagem.objects.all()
  serializer_class = PostagemSerializer