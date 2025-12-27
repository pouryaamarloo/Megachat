from django.contrib import admin
from django.urls import path, include

from .views import MessageViewSet

from rest_framework.routers import DefaultRouter
from .views import MessageViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet, basename='messages')

urlpatterns = router.urls