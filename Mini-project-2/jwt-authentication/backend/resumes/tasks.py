from celery import shared_task
from .models import Resume
from pymongo import MongoClient
import spacy

@shared_task
def parse_resume_ai(resume_id):
    resume = Resume.objects.get(id=resume_id)
    # Placeholder NLP logic
    nlp = spacy.load("en_core_web_sm")
    parsed_result = {
        "skills": ["Python", "Django"],
        "experience": "3 years",
        "education": "BSc Computer Science"
    }

    # Save parsed result to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["resume_ai"]
    collection = db["parsed_resumes"]
    collection.insert_one({"resume_id": resume.id, **parsed_result})

    resume.parsed_data = parsed_result
    resume.save()