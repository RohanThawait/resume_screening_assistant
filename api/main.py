from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from app.pdf_parser import extract_text_from_pdf
from app.model import rank_resumes
import tempfile

app = FastAPI(title="Resume Screening Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/rank/")
async def rank_endpoint(
    job_description: str = Form(...),
    resumes: List[UploadFile] = File(...)
):
    resume_texts = {}

    for resume in resumes:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(await resume.read())
            tmp_path = tmp.name
        
        # Parse text
        text = extract_text_from_pdf(tmp_path)
        resume_texts[resume.filename] = text

    # Rank resumes
    ranked = rank_resumes(job_description, resume_texts)
    return {"ranked_resumes": ranked}
