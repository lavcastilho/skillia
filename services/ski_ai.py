from services.matcher import calculate_match

VACANCIES = [

    {
        "title": "Desenvolvedor Python Júnior",
        "company": "TechNova",
        "skills": ["python", "flask", "sql", "git"]
    },

    {
        "title": "Frontend Developer",
        "company": "UI Future",
        "skills": ["html", "css", "javascript", "react"]
    },

    {
        "title": "Analista de Dados",
        "company": "DataVision",
        "skills": ["python", "sql", "power bi", "excel"]
    },

    {
        "title": "DevOps Jr",
        "company": "CloudSync",
        "skills": ["docker", "aws", "linux", "git"]
    }

]


def recommend(user_skills):

    results = []

    for v in VACANCIES:

        score = calculate_match(
            user_skills,
            v["skills"]
        )

        results.append({
            "title": v["title"],
            "company": v["company"],
            "match": score
        })

    results.sort(
        key=lambda x: x["match"],
        reverse=True
    )

    return results