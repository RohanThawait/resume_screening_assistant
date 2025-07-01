from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from app.utils import load_json

model = SentenceTransformer("all-MiniLM-L6-v2")  # Fast and good enough

def rank_resumes(job_description: str, resume_dict: dict, top_k=5):
    resume_names = list(resume_dict.keys())
    resume_texts = list(resume_dict.values())

    # Encode job description and resumes
    job_embedding = model.encode([job_description])
    resume_embeddings = model.encode(resume_texts)

    # Compute cosine similarity
    similarities = cosine_similarity(job_embedding, resume_embeddings)[0]

    # Rank resumes by score
    ranked_indices = np.argsort(similarities)[::-1][:top_k]
    ranked_resumes = [
        {"resume": resume_names[i], "score": float(similarities[i])}
        for i in ranked_indices
    ]
    return ranked_resumes
