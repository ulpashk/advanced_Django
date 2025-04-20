import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resume_ai_platform.settings')

app = Celery('resume_ai_platform')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
