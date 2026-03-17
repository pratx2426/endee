 ## Smart AI Career Assistant (Endee-Based Project)

## Project Overview
This project is an AI-powered career assistant that helps users analyze their resumes and find the most suitable job roles.

It uses semantic search and vector-based similarity to match resumes with job descriptions, identify missing skills, and generate a personalized career improvement roadmap.


##  Problem Statement
Students often struggle to understand:
- Which job roles they are best suited for
- What skills they are missing
- How to improve their profile

This project solves that by providing **AI-driven career insights**.

##  System Design

### 🔹 Step 1: Input
- User uploads a resume (PDF) or pastes text

### 🔹 Step 2: Embedding Generation
- Resume and job descriptions are converted into vector embeddings using `SentenceTransformers`

### 🔹 Step 3: Similarity Search
- Cosine similarity is used to compare resume embeddings with job embeddings
- Top matching jobs are retrieved

### 🔹 Step 4: Skill Gap Analysis
- Extracts required skills from job descriptions
- Compares with resume content
- Identifies missing skills

### 🔹 Step 5: Recommendation Engine
- Suggests skills to learn
- Generates a 30-day career roadmap

##  Use of Endee (Vector Database)

This project is designed based on the core principles of vector databases like Endee:

- Data is converted into high-dimensional embeddings
- Similarity search is used for retrieval
- Relevant results are fetched based on semantic meaning rather than keyword matching

Currently, embeddings are handled in-memory for simplicity.  
However, the architecture is fully compatible with Endee, where:

- Job embeddings can be stored in Endee
- Resume queries can be executed using vector search
- Results can be retrieved efficiently at scale

---

##  Features

-  Semantic job matching (AI-based)
-  Resume PDF upload
-  Skill gap analysis
-  Learning recommendations
-  Career roadmap generator
-  Clean Streamlit UI

## Tech Stack

- Python
- Streamlit
- Sentence Transformers
- Scikit-learn
- PyPDF2


## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/pratx2426/endee.git
cd endee