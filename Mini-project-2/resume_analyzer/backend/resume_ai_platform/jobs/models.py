from django.db import models
from django.conf import settings

class JobListing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    skills_required = models.JSONField()  # List of skills required for the job
    experience_required = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Recruiter posting the job
    posted_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title
