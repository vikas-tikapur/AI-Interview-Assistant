import pdfplumber
from docx import Document


def extract_text_from_pdf(file_path):

    text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_text_from_docx(file_path):

    doc = Document(file_path)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def extract_skills(text):

    skills_database = [
        "Python",
        "OpenCV",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "YOLO",
        "MySQL",
        "Pandas",
        "NumPy",
        "HTML",
        "CSS",
        "JavaScript",
        "WordPress",
        "MediaPipe"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_database:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills
