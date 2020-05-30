from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from heyjoyce.users.views import UserViewSet
from heyjoyce.posts.views import PostViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]