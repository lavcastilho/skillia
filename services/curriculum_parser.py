import PyPDF2

SKILLS_DATABASE = [

    "python",
    "java",
    "javascript",
    "react",
    "node",
    "sql",
    "postgresql",
    "mysql",
    "mongodb",
    "flask",
    "django",
    "git",
    "docker",
    "aws",
    "azure",
    "power bi",
    "excel",
    "figma",
    "html",
    "css"

]

def extract_text(pdf_path):

    text = ""

    with open(pdf_path, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    return text.lower()

def detect_skills(text):

    found_skills = []

    for skill in SKILLS_DATABASE:

        if skill in text:
            found_skills.append(skill)

    return found_skills