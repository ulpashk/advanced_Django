from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Resume
from .serializers import ResumeUploadSerializer
from .tasks import parse_resume_ai

class ResumeUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ResumeUploadSerializer(data=request.data)
        if serializer.is_valid():
            resume = serializer.save(user=request.user)
            parse_resume_ai.delay(resume.id)  # Celery task
            return Response({'message': 'Resume uploaded, parsing started.'}, status=201)
        return Response(serializer.errors, status=400)
