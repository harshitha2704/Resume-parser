import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import fitz
import docx2txt
import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(file_path):
    text = ""
    pdf_document = fitz.open(file_path)
    for page in pdf_document:
        text += page.get_text()
    return text

def calculate_similarity(job_description, resume_text):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # Load pre-trained BERT model
    job_embedding = model.encode([job_description])[0]
    resume_embedding = model.encode([resume_text])[0]

    job_embedding = job_embedding.reshape(1, -1)  # Reshape embeddings for similarity calculation
    resume_embedding = resume_embedding.reshape(1, -1)

    similarity = cosine_similarity(job_embedding, resume_embedding)[0][0]
    return similarity

def process_job_and_resumes():
    job_file = filedialog.askopenfilename(title="Select Job Description File", filetypes=[("Text Files", "*.txt")])
    if not job_file:
        messagebox.showwarning("Warning", "Please select a job description file.")
        return

    job_description = ""
    with open(job_file, 'r') as f:
        job_description = f.read()

    resume_files = filedialog.askopenfilenames(title="Select Resume Files", filetypes=[("PDF Files", "*.pdf"), ("Word Files", "*.docx")])
    if not resume_files:
        messagebox.showwarning("Warning", "Please select at least one resume file.")
        return

    similarity_scores = []
    for resume_file in resume_files:
        file_name = os.path.basename(resume_file)
        if resume_file.lower().endswith(('.pdf', '.docx')):
            if resume_file.lower().endswith('.pdf'):
                resume_text = extract_text_from_pdf(resume_file)
            else:
                resume_text = docx2txt.process(resume_file)
            
            similarity = calculate_similarity(job_description, resume_text)
            similarity_scores.append((file_name, similarity))

    if similarity_scores:
        similarity_scores.sort(key=lambda x: x[1], reverse=True)
        top_matches = similarity_scores[:3]  

        result_window = tk.Toplevel(root)
        result_window.title("Matching Scores")

        title_label = tk.Label(result_window, text="Top Matching Resumes", font=("Arial", 16, "bold"), fg="blue")
        title_label.pack(pady=10)

        for resume, score in top_matches:
            result_label = tk.Label(result_window, text=f"{resume} - Similarity Score: {score:.2f}", font=("Arial", 12), fg="green")
            result_label.pack()
    else:
        messagebox.showinfo("Information", "No matching resumes found.")

root = tk.Tk()
root.title("Enhanced Resume Parser")

header_label = tk.Label(root, text="Welcome to Enhanced Resume Parser", font=("Arial", 20, "bold"), fg="black")
header_label.pack(pady=20)

process_button = tk.Button(root, text="Select Job Description and Resumes", command=process_job_and_resumes, font=("Arial", 12))
process_button.pack(pady=10)

root.mainloop()
