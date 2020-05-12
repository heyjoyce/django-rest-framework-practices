from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter(trailing_slash=False)
router.register(r'articles', views.ArticlesViewSet, basename='article')

urlpatterns = [
    path('', include(router.urls)),
]