from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api.viewsets import PostagemViewSet

router = DefaultRouter()

router.register("postagens", PostagemViewSet)

urlpatterns = [
    path('', include(router.urls))
]
