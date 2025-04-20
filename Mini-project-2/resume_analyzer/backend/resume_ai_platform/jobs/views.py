from django.shortcuts import render
from rest_framework import viewsets
from .models import JobListing
from .serializers import JobListingSerializer
from rest_framework.permissions import IsAuthenticated

class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users (Recruiters) can create and edit job listings

    def perform_create(self, serializer):
        # Ensure the job is posted by the authenticated user (Recruiter)
        serializer.save(posted_by=self.request.user)
