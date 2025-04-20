from django.shortcuts import render

class ResumeUploadView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ResumeUploadSerializer(data=request.data)
        if serializer.is_valid():
            resume = serializer.save(user=request.user)
            parse_resume_task.delay(resume.id)  # Call Celery task
            return Response({'status': 'Resume uploaded'}, status=201)
        return Response(serializer.errors, status=400)