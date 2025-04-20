from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# from celery import shared_task
# from .tasks import parse_resume_task


class ResumeUpload(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/files')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='PENDING')  # PENDING, PROCESSING, COMPLETED, FAILED
    parsed_data_id = models.CharField(max_length=100, blank=True, null=True)  # MongoDB ObjectId

    def save(self, *args, **kwargs):
        if not self.id:  # If it's a new resume (not already saved)
            self.status = 'PENDING'
        super().save(*args, **kwargs)

@receiver(post_save, sender=ResumeUpload)
def trigger_resume_parsing(sender, instance, created, **kwargs):
    if created:
        # Importing here to avoid circular import
        from .tasks import parse_resume_task
        parse_resume_task.delay(instance.id)




# class ResumeUpload(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     file = models.FileField(upload_to='resumes/files')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, default='PENDING')  # PENDING, PROCESSING, COMPLETED, FAILED
#     parsed_data_id = models.CharField(max_length=100, blank=True, null=True)  # MongoDB ObjectId
