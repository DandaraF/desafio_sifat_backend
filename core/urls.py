from django.urls import path, include
from rest_framework.routers import SimpleRouter

from core.api.viewsets import PostagemViewSet

router = SimpleRouter(trailing_slash=False)

router.register("api", PostagemViewSet)

urlpatterns = [
    path('', include(router.urls))
]
