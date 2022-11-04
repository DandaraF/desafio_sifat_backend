from rest_framework.viewsets import ModelViewSet

from core.models import Postagem
from .serializers import PostagemSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PostagemViewSet(ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['titulo', 'texto', 'categoria']
