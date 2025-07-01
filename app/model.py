from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Don't load at module level
_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model

def rank_resumes(job_description: str, resume_dict: dict, top_k=5):
    model = get_model()

    resume_names = list(resume_dict.keys())
    resume_texts = list(resume_dict.values())

    job_embedding = model.encode([job_description])
    resume_embeddings = model.encode(resume_texts)

    similarities = cosine_similarity(job_embedding, resume_embeddings)[0]
    ranked_indices = np.argsort(similarities)[::-1][:top_k]

    ranked_resumes = [
        {"resume": resume_names[i], "score": float(similarities[i])}
        for i in ranked_indices
    ]
    return ranked_resumes
