from django.urls import path
from .views import ResumeUploadView, ResumeSearchBySkillsView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', ResumeUploadView.as_view(), name='upload-resume'),
    path('search/', ResumeSearchBySkillsView.as_view(), name='resume-search-skills'),
]

# urlpatterns = [
#     path('upload/', ResumeUploadView.as_view(), name='upload-resume'),
#     path('search/', ResumeSearchBySkillsView.as_view(), name='resume-search-skills'),
#     path('uploadd/', views.upload_resume, name='upload_resume'),
#     path('status/<int:resume_id>/', views.check_resume_status, name='check_resume_status'),
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)