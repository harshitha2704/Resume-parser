import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import fitz
import docx2txt
import os
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize


def extract_text_from_pdf(file_path):
    text = ""
    pdf_document = fitz.open(file_path)
    for page in pdf_document:
        text += page.get_text()
    return text

def calculate_similarity(job_description, resume_text):
    job_tokens = word_tokenize(job_description.lower())
    resume_tokens = word_tokenize(resume_text.lower())

    job_model = Word2Vec([job_tokens], min_count=1, vector_size=100)
    resume_model = Word2Vec([resume_tokens], min_count=1, vector_size=100)

    similarity = job_model.wv.n_similarity(job_tokens, resume_tokens)
    similarity_percentage = similarity * 100
    return similarity_percentage

def process_job_and_resumes():
    job_file = filedialog.askopenfilename(title="Select Job Description File", filetypes=[("Text Files", "*.txt")])
    if not job_file:
        messagebox.showwarning("Warning", "Please select a job description file.")
        return

    job_description = ""
    with open(job_file, 'r') as f:
        job_description = f.read()

    resume_files = filedialog.askopenfilenames(title="Select Resume Files", filetypes=[("PDF Files", "*.pdf")])
    if not resume_files:
        messagebox.showwarning("Warning", "Please select at least one resume file.")
        return

    similarity_scores = []
    for resume_file in resume_files:
       
        file_name = os.path.basename(resume_file)
        if resume_file.lower().endswith('.pdf'):
            resume_text = extract_text_from_pdf(resume_file)
        else:
            resume_text = docx2txt.process(resume_file)
        
        similarity = calculate_similarity(job_description, resume_text)
        similarity_scores.append((file_name, similarity))

    similarity_scores.sort(key=lambda x: x[1], reverse=True)
    top_matches = similarity_scores[:3]  

    result_window = tk.Toplevel(root)
    result_window.title("Matching Scores")

    title_label = tk.Label(result_window, text="Top Matching Resumes", font=("Arial", 16, "bold"), fg="blue")
    title_label.pack(pady=10)

    for resume, score in top_matches:
        result_label = tk.Label(result_window, text=f"{resume} - Similarity Score: {score:.2f}%", font=("Arial", 12), fg="green")
        result_label.pack()


root = tk.Tk()
root.title("ProficiencyAligner")

header_label = tk.Label(root, text="Welcome to Proficiency Aligner", font=("Arial", 20, "bold"), fg="black")
header_label.pack(pady=20)

process_button = tk.Button(root, text="Select Job Description and Resumes", command=process_job_and_resumes, font=("Arial", 12))
process_button.pack(pady=10)

root.mainloop()
