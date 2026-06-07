def calculate_match(user_skills, vacancy_skills):

    if not user_skills:
        return 0

    user_set = set(user_skills)
    vacancy_set = set(vacancy_skills)

    common = user_set.intersection(vacancy_set)

    score = (len(common) / len(vacancy_set)) * 100

    return round(score, 2)