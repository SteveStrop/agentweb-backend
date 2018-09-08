from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')  # displayed in Django API root
router.register('profile', views.UserProfileViewSet)  # displayed in Django API root (127.0.0.1:8080/api/)

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),  # points to an APIView
    url(r'', include(router.urls)),  # points to all viewsets
]
