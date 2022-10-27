from rest_framework.routers import DefaultRouter
from .api.viewsets import PostagemViewSet
from django.urls import path, include
router = DefaultRouter()

router.register("postagens", PostagemViewSet)

urlpatterns = [
    path('', include(router.urls))
]
