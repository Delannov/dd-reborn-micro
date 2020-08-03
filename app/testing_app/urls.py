from django.urls import path, include

from rest_framework.routers import DefaultRouter

from testing_app import views

router = DefaultRouter()
router.register('hello', views.HelloViewSet, base_name='hello')

urlpatterns = [
    path('', include(router.urls)),
]
