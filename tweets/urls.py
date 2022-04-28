from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api', StudentsViewSet)

urlpatterns = [
    path('', include(router.urls) )
]
