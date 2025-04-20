from rest_framework import serializers
from .models import ResumeUpload

class ResumeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeUpload
        fields = ['id', 'file', 'uploaded_at', 'status']
        read_only_fields = ['uploaded_at', 'status']
