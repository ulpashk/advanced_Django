from django.db import models
# Create your models here.
from django.conf import settings

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')
    parsed_data = models.JSONField(null=True, blank=True)  # MongoDB logic handled separately
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume - {self.user.email}"
