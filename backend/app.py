from flask import Flask, request, jsonify
from flask_cors import CORS
from pdfminer.high_level import extract_text
import os

app = Flask(__name__)
CORS(app)

def parse_resume(file_path):
    text = extract_text(file_path)
    return text

# Dummy job database
job_keywords = {
    "Python Developer": ["python", "django", "flask", "api"],
    "Frontend Developer": ["html", "css", "javascript", "react"],
    "Data Scientist": ["machine learning", "pandas", "numpy", "regression"],
    "AI/ML Engineer": ["deep learning", "tensorflow", "nlp", "neural network"],
    "Backend Developer": ["node.js", "express", "mongodb", "api"],
    "Full Stack Developer": ["frontend", "backend", "database", "react", "flask"],
    "DevOps Engineer": ["docker", "kubernetes", "ci/cd", "jenkins"],
    "Database Admin": ["sql", "database", "queries", "mysql", "postgres"],
}

def recommend_jobs(resume_text):
    resume_text = resume_text.lower()
    matched_jobs = []
    for job, keywords in job_keywords.items():
        if any(keyword in resume_text for keyword in keywords):
            matched_jobs.append(job)
    return matched_jobs

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['resume']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(filepath)

    extracted_text = parse_resume(filepath)
    recommendations = recommend_jobs(extracted_text)

    return jsonify({
        "resume_text": extracted_text,
        "recommendations": recommendations
    })

if __name__ == '__main__':
    app.run(debug=True)
