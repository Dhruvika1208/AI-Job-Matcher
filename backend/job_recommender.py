# job_recommender.py

import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_PATH = 'data/job_roles.json'

def load_job_roles():
    with open(DATA_PATH, 'r') as file:
        return json.load(file)

def recommend_jobs(resume_text, top_n=5):
    job_data = load_job_roles()
    roles = [job['description'] for job in job_data]
    titles = [job['title'] for job in job_data]

    tfidf = TfidfVectorizer(stop_words='english')
    vectors = tfidf.fit_transform([resume_text] + roles)

    similarity_scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    top_indices = similarity_scores.argsort()[::-1][:top_n]

    recommendations = [titles[i] for i in top_indices]
    return recommendations
