from urllib.parse import urlencode

def generate_assessment_link(student_id: str, quiz_id: str) -> str:
    base_url = "http://127.0.0.1:8080/quiz/assessments"
    query_params = {
        "student_id": student_id,
        "quiz_id": quiz_id
    }
    
    assessment_link = f"{base_url}?{urlencode(query_params)}"
    return assessment_link