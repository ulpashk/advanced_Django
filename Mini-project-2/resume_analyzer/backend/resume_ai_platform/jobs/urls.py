from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobListingViewSet

router = DefaultRouter()
router.register(r'job-listings', JobListingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
