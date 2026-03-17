import PyPDF2
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

st.markdown("### 🚀 Smart AI Career Assistant")
st.caption("Analyze your resume, find job matches, and improve your skills")


jobs = pd.read_csv("jobs.csv")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

resume = ""

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    for page in pdf_reader.pages:
        resume += page.extract_text()


if st.button("Analyze"):
    if resume.strip() == "":
        st.warning("Please enter your resume")
    else:
        st.subheader("Top Job Matches (AI Powered)")

        job_descriptions = jobs["description"].tolist()
        job_vectors = model.encode(job_descriptions)
        resume_vector = model.encode([resume])
        from sklearn.metrics.pairwise import cosine_similarity
        similarity = cosine_similarity(resume_vector, job_vectors).flatten()

        jobs["score"] = similarity
        top_jobs = jobs.sort_values(by="score", ascending=False).head(3)

        for _, row in top_jobs.iterrows():
            st.write(f"### {row['job_title']}")
            st.write(f"Match Score: {round(row['score']*100, 2)}%")
            job_skills = [skill.strip().lower() for skill in row['description'].split(",")]
            resume_words = resume.lower().split()
            missing_skills = [skill for skill in job_skills if skill not in resume_words]
            st.write(f"Required Skills: {row['description']}")
            if missing_skills:
                st.write("❌ Missing Skills:")
                st.write(", ".join(missing_skills))
                st.write("💡 Suggested Learning Path:")
                for skill in missing_skills:
                    st.write(f"- Learn {skill}")
                st.write("📈 Career Roadmap (30 Days Plan):")
                for i, skill in enumerate(missing_skills[:3]):
                    st.write(f"Week {i+1}: Focus on {skill}")

            else:
                st.write("✅ You have most required skills!")
                st.write("---")