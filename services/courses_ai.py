def recommend_courses(skills):

    courses = []

    if "python" in skills:
        courses.append("Curso de Python Avançado")

    if "react" in skills:
        courses.append("React do Zero ao Avançado")

    if "sql" in skills:
        courses.append("Banco de Dados SQL Completo")

    if "docker" in skills:
        courses.append("Docker para Iniciantes")

    return courses