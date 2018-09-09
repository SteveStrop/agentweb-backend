from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')  # displayed in Django API root
router.register('profile', views.UserProfileViewSet)  # displayed in Django API root (127.0.0.1:8080/api/)
router.register('login', views.LoginViewSet, base_name='login') # this is how client will recognise it
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),  # points to an APIView
    url(r'^radioDestinations/', views.RadioDestinationsApiView.as_view()),  # points to an APIView
    url(r'', include(router.urls)),  # points to all viewsets
]
