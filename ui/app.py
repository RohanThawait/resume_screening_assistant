import streamlit as st
import requests

st.set_page_config(page_title="Resume Screener", layout="centered")

st.title("🧠 Resume Screening Assistant")

# --- Job Description Input ---
job_description = st.text_area("Paste the Job Description here:")

# --- Resume Upload ---
uploaded_files = st.file_uploader(
    "Upload Resumes (PDFs)",
    type=["pdf"],
    accept_multiple_files=True
)

# --- Submit ---
if st.button("🔍 Rank Resumes"):
    if not job_description or not uploaded_files:
        st.warning("Please provide a job description and at least one resume.")
    else:
        with st.spinner("Processing..."):

            # Prepare files for API
            files = [("resumes", (f.name, f.read(), "application/pdf")) for f in uploaded_files]
            data = {"job_description": job_description}

            # Call backend API
            try:
                response = requests.post(
                    "http://localhost:8000/rank/",
                    data=data,
                    files=files
                )
                result = response.json()

                # Display results
                st.success("Top Matching Resumes:")
                for i, item in enumerate(result["ranked_resumes"], start=1):
                    st.write(f"**{i}. {item['resume']}** — Score: `{item['score']:.3f}`")

            except Exception as e:
                st.error(f"Failed to connect to API: {e}")
