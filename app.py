from flask import Flask, render_template, request
import os
import re
import pdfplumber
from docx import Document

app = Flask(__name__)

UPLOAD_FOLDER = 'resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# ---------------- HOME PAGE ---------------- #

@app.route('/')
def index():

    return render_template('index.html')


# ---------------- UPLOAD PAGE ---------------- #

@app.route('/upload')
def upload_page():

    return render_template('upload.html')


# ---------------- READ PDF ---------------- #

def extract_text_from_pdf(filepath):

    text = ""

    with pdfplumber.open(filepath) as pdf:

        for page in pdf.pages:

            text += page.extract_text()

    return text


# ---------------- READ DOCX ---------------- #

def extract_text_from_docx(filepath):

    doc = Document(filepath)

    text = ""

    for para in doc.paragraphs:

        text += para.text

    return text


# ---------------- EXTRACT EMAIL ---------------- #

def extract_email(text):

    email = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return email[0] if email else "Not Found"


# ---------------- EXTRACT PHONE ---------------- #

def extract_phone(text):

    phone = re.findall(
        r"\+?\d[\d -]{8,12}\d",
        text
    )

    return phone[0] if phone else "Not Found"


# ---------------- EXTRACT NAME ---------------- #

def extract_name(text):

    lines = text.split('\n')

    for line in lines:

        line = line.strip()

        # Ignore numbers or short lines

        if (
            len(line) > 2
            and not line.isdigit()
            and '@' not in line
            and '+' not in line
        ):

            return line

    return "Name Not Found"


# ---------------- DETECT SKILLS ---------------- #

def extract_skills(text):

    skills_list = [

        "Python",
        "Java",
        "Machine Learning",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Flask",
        "Communication",
        "Leadership",
        "Data Analysis"

    ]

    found_skills = []

    for skill in skills_list:

        if skill.lower() in text.lower():

            found_skills.append(skill)

    return found_skills


# ---------------- DETECT ROLE ---------------- #

def detect_role(skills):

    if "Machine Learning" in skills:

        return "AI / ML Engineer"

    elif "React" in skills:

        return "Frontend Developer"

    elif "Flask" in skills:

        return "Python Developer"

    elif "Data Analysis" in skills:

        return "Data Analyst"

    else:

        return "Software Professional"


# ---------------- ANALYZE RESUME ---------------- #

@app.route('/analyze', methods=['POST'])
def analyze():

    resume = request.files['resumeFile']

    if resume:

        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'],
            resume.filename
        )

        resume.save(filepath)

        # READ RESUME

        if resume.filename.endswith('.pdf'):

            resume_text = extract_text_from_pdf(filepath)

        elif resume.filename.endswith('.docx'):

            resume_text = extract_text_from_docx(filepath)

        else:

            resume_text = ""


        # EXTRACT DETAILS

        name = extract_name(resume_text)

        email = extract_email(resume_text)

        phone = extract_phone(resume_text)

        skills = extract_skills(resume_text)

        role = detect_role(skills)

        score = 87

        summary = (
            "AI analyzed the uploaded resume and "
            "detected candidate skills successfully."
        )

        return render_template(

            'result.html',

            name=name,
            email=email,
            phone=phone,
            role=role,
            filename=resume.filename,
            score=score,
            skills=skills,
            summary=summary

        )

    return "Upload Failed"


# ---------------- RUN APP ---------------- #

if __name__ == '__main__':

    app.run(debug=True)