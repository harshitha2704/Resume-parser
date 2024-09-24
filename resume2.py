# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity
# import fitz
# import docx2txt
# import os

# def extract_text_from_pdf(file_path):
#     text = ""
#     pdf_document = fitz.open(file_path)
#     for page in pdf_document:
#         text += page.get_text()
#     return text
#     print(text)

# def calculate_similarity(job_description, resume_text):
#     model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # Load pre-trained BERT model
#     job_embedding = model.encode([job_description])[0]
#     resume_embedding = model.encode([resume_text])[0]

#     similarity = cosine_similarity([job_embedding], [resume_embedding])[0][0]
#     similarity_percentage = similarity * 100
#     return similarity_percentage

# def process_job_and_resumes():
#     job_file = filedialog.askopenfilename(title="Select Job Description File", filetypes=[("Text Files", "*.txt")])
#     if not job_file:
#         messagebox.showwarning("Warning", "Please select a job description file.")
#         return

#     job_description = ""
#     with open(job_file, 'r') as f:
#         job_description = f.read()

#     resume_files = filedialog.askopenfilenames(title="Select Resume Files", filetypes=[("PDF Files", "*.pdf"), ("Word Files", "*.docx")])
#     if not resume_files:
#         messagebox.showwarning("Warning", "Please select at least one resume file.")
#         return

#     similarity_scores = []
#     for resume_file in resume_files:
#         file_name = os.path.basename(resume_file)
#         if resume_file.lower().endswith(('.pdf', '.docx')):
#             if resume_file.lower().endswith('.pdf'):
#                 resume_text = extract_text_from_pdf(resume_file)
#             else:
#                 resume_text = docx2txt.process(resume_file)
            
#             similarity = calculate_similarity(job_description, resume_text)
#             similarity_scores.append((file_name, similarity))

#     if similarity_scores:
#     # Sort similarity scores in descending order based on similarity score (second element)
#         similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

#         top_resumes = similarity_scores[:5]  # Get the top five resumes

#         result_window = tk.Toplevel(root)
#         result_window.title("Top Three Resume Scores")

#         title_label = tk.Label(result_window, text="Top Three Resume Scores", font=("Arial", 16, "bold"), fg="blue")
#         title_label.pack(pady=10)

#         for resume, score in top_resumes:
#             result_label = tk.Label(result_window, text=f"{resume} - Similarity Score: {score:.2f}%", font=("Arial", 12), fg="green")
#             result_label.pack()
#     else:
#         messagebox.showinfo("Information", "No matching resumes found.")

# root = tk.Tk()
# root.title("resume parser")

# header_label = tk.Label(root, text="Welcome to Resume Parser", font=("Arial", 20, "bold"), fg="black")
# header_label.pack(pady=20)
# print(header_label)
# process_button = tk.Button(root, text="Select Job Description and Resumes", command=process_job_and_resumes, font=("Arial", 12))
# print(process_button)
# process_button.pack(pady=10)

# root.mainloop()

# import tkinter as tk
# from tkinter import filedialog, messagebox
# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity
# import fitz
# import docx2txt
# import os

# def extract_text_from_pdf(file_path):
#     text = ""
#     pdf_document = fitz.open(file_path)
#     for page in pdf_document:
#         text += page.get_text()
#     return text

# def calculate_similarity(job_description, resume_text):
#     job_description_lower = job_description.lower()
#     resume_text_lower = resume_text.lower()

#     if not job_description_lower or not resume_text_lower:
#         return 0  # Return 0 if either the job description or resume text is empty

#     model = SentenceTransformer('all-MiniLM-L6-v2')
#     job_embedding = model.encode([job_description_lower])[0]
#     resume_embedding = model.encode([resume_text_lower])[0]

#     similarity = cosine_similarity([job_embedding], [resume_embedding])[0][0]
#     similarity_percentage = similarity * 100

#     # Introduce a threshold (adjust as needed)
#     threshold = 50
#     if similarity_percentage < threshold:
#         similarity_percentage = 0  # Set the similarity to 0 if below the threshold

#     return similarity_percentage

# def process_job_and_resumes():
#     job_file = filedialog.askopenfilename(title="Select Job Description File", filetypes=[("Text Files", "*.txt")])
#     if not job_file:
#         messagebox.showwarning("Warning", "Please select a job description file.")
#         return

#     job_description = ""
#     with open(job_file, 'r') as f:
#         job_description = f.read()

#     resume_files = filedialog.askopenfilenames(title="Select Resume Files", filetypes=[("PDF Files", "*.pdf"), ("Word Files", "*.docx")])
#     if not resume_files:
#         messagebox.showwarning("Warning", "Please select at least one resume file.")
#         return

#     similarity_scores = []
#     for resume_file in resume_files:
#         file_name = os.path.basename(resume_file)
#         if resume_file.lower().endswith(('.pdf', '.docx')):
#             if resume_file.lower().endswith('.pdf'):
#                 resume_text = extract_text_from_pdf(resume_file)
#             else:
#                 resume_text = docx2txt.process(resume_file)

#             similarity = calculate_similarity(job_description, resume_text)
#             similarity_scores.append((file_name, similarity))

#     if similarity_scores:
#         similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[:3]

#         result_window = tk.Toplevel(root)
#         result_window.title("Top Three Resume Scores")

#         title_label = tk.Label(result_window, text="Top Three Resume Scores", font=("Arial", 16, "bold"), fg="blue")
#         title_label.pack(pady=10)

#         for resume, score in similarity_scores:
#             result_label = tk.Label(result_window, text=f"{resume} - Similarity Score: {score:.2f}%", font=("Arial", 12), fg="green")
#             result_label.pack()
#     else:
#         messagebox.showinfo("Information", "No matching resumes found.")

# root = tk.Tk()
# root.title("Resume Parser")

# header_label = tk.Label(root, text="Welcome to Resume Parser", font=("Arial", 20, "bold"), fg="black")
# header_label.pack(pady=20)

# process_button = tk.Button(root, text="Select Job Description and Resumes", command=process_job_and_resumes, font=("Arial", 12))
# process_button.pack(pady=10)

# root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import fitz
import docx2txt
import os

def extract_text_from_pdf(file_path):
    text = ""
    pdf_document = fitz.open(file_path)
    for page in pdf_document:
        text += page.get_text()
    return text

def calculate_similarity(job_description, resume_text):
    if job_description and resume_text:  # Check if both job description and resume text are non-empty
        # Updated to a more powerful pre-trained model
        model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        job_embedding = model.encode([job_description])[0]
        resume_embedding = model.encode([resume_text])[0]

        similarity = cosine_similarity([job_embedding], [resume_embedding])[0][0]
        similarity_percentage = similarity*100

        return similarity_percentage
    else:
        return 0  # Return 0 if either the job description or resume text is empty

def process_job_and_resumes():
    job_file = filedialog.askopenfilename(title="Select Job Description File", filetypes=[("Text Files", "*.txt")])
    if not job_file:
        messagebox.showwarning("Warning", "Please select a job description file.")
        return

    job_description = ""
    with open(job_file, 'r') as f:
        job_description = f.read()
    print(job_description)
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

            # Updated: Normalize text to lowercase for better consistency
            job_description_lower = job_description.lower()
            resume_text_lower = resume_text.lower()

            similarity = calculate_similarity(job_description_lower, resume_text_lower)
            similarity_scores.append((file_name, similarity))

    if similarity_scores:
        # Updated: Sort by similarity score and take the top three
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[:3]

        result_window = tk.Toplevel(root)
        result_window.title("Top Three Resume Scores")

        title_label = tk.Label(result_window, text="Top Three Resume Scores", font=("Arial", 16, "bold"), fg="blue")
        title_label.pack(pady=10)

        for resume, score in similarity_scores:
            result_label = tk.Label(result_window, text=f"{resume} - Similarity Score: {score:.2f}%", font=("Arial", 12), fg="green")
            result_label.pack()
    else:
        messagebox.showinfo("Information", "No matching resumes found.")

root = tk.Tk()
root.title("Resume Parser")

header_label = tk.Label(root, text="Welcome to Resume Parser", font=("Arial", 20, "bold"), fg="black")
header_label.pack(pady=20)

process_button = tk.Button(root, text="Select Job Description and Resumes", command=process_job_and_resumes, font=("Arial", 12))
process_button.pack(pady=10)


root.mainloop()
