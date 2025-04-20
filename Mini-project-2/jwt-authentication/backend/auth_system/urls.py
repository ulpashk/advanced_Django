from django.urls import path, include, re_path
from django.views.generic import TemplateView

from resumes.views import ResumeUploadView
from rest_framework.routers import DefaultRouter
from jobs.views import JobListingViewSet


router = DefaultRouter()
router.register(r'jobs', JobListingViewSet, basename='job')

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('', include('accounts.urls')),  # or your app name here
    path('api/resume/upload/', ResumeUploadView.as_view(), name='resume-upload'),
    path('api/', include(router.urls)),
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]


# router = DefaultRouter()
# router.register(r'jobs', JobListingViewSet, basename='job')

# urlpatterns = [
#     path('api/resume/upload/', ResumeUploadView.as_view(), name='resume-upload'),
#     path('api/', include(router.urls)),
# ]
