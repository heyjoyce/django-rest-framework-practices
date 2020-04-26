from rest_framework.routers import DefaultRouter
from . import views

app_name = 'articles'

router = DefaultRouter()
router.register('', views.ArticlesViewSet)
urlpatterns = router.urls
