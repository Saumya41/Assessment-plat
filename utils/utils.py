
from urllib.parse import urlencode

def generate_assessment_link(student_id: str, quiz_id: str) -> str:
    base_url = "https://yourdomain.com/assessments"  # Replace with your actual domain
    query_params = {
        "student_id": student_id,
        "quiz_id": quiz_id,
        "token": "some_unique_secure_token"  # Optional: Add a secure token for validation
    }
    
    assessment_link = f"{base_url}?{urlencode(query_params)}"
    return assessment_link
