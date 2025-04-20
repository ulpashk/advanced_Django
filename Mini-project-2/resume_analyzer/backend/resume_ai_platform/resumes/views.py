from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import ResumeUpload
from .serializers import ResumeUploadSerializer
from .tasks import parse_resume_task
from pymongo import MongoClient
from django.conf import settings


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os



class ResumeUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ResumeUploadSerializer(data=request.data)
        if serializer.is_valid():
            resume = serializer.save(user=request.user)
            parse_resume_task.delay(resume.id)
            return Response({"message": "Resume uploaded and parsing started."}, status=201)
        return Response(serializer.errors, status=400)



class ResumeSearchBySkillsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        skills = request.query_params.getlist('skill[]')
        if not skills:
            return Response({"error": "Please provide at least one skill as a query parameter."}, status=400)

        # Connect to MongoDB
        client = MongoClient(settings.MONGO_URI)
        db = client[settings.MONGO_DB_NAME]
        collection = db.resumes

        # MongoDB query
        query = {"skills": {"$all": skills}}
        results = list(collection.find(query, {"_id": 0}))  # exclude _id for simplicity

        return Response({"results": results})



# @csrf_exempt
# def upload_resume(request):
#     if request.method == 'POST':
#         file = request.FILES.get('file')
#         if file:
#             resume = ResumeUpload.objects.create(user=request.user, file=file)
#             # Trigger Celery task to parse the resume
#             parse_resume_task.delay(resume.id)
#             return JsonResponse({"id": resume.id}, status=201)

#         return JsonResponse({"error": "No file provided."}, status=400)


# def check_resume_status(request, resume_id):
#     try:
#         resume = ResumeUpload.objects.get(id=resume_id)
#         return JsonResponse({
#             "status": resume.status,
#             "parsed_data": resume.parsed_data if resume.status == 'COMPLETED' else None
#         })
#     except ResumeUpload.DoesNotExist:
#         return JsonResponse({"error": "Resume not found."}, status=404)



# def filter_resumes(request):
#     skills = request.GET.get('skills', None)
#     location = request.GET.get('location', None)
#     experience = request.GET.get('experience', None)

#     resumes = ResumeUpload.objects.all()

#     if skills:
#         resumes = resumes.filter(parsed_data__skills__contains=skills)
#     if location:
#         resumes = resumes.filter(parsed_data__location__contains=location)
#     if experience:
#         resumes = resumes.filter(parsed_data__experience__contains=experience)

#     # Add your pagination or any additional processing here
#     return JsonResponse({"resumes": [resume.to_dict() for resume in resumes]})