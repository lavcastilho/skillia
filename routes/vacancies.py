from flask import Blueprint
from flask import render_template

from flask_login import login_required, current_user

from models.profile import Profile
from services.ski_ai import recommend

vacancies_bp = Blueprint("vacancies", __name__)


@vacancies_bp.route("/vacancies")
@login_required
def vacancies():

    profile = Profile.query.filter_by(
        user_id=current_user.id
    ).first()

    skills = []

    if profile and profile.detected_skills:
        skills = profile.detected_skills.split(",")

    recommendations = recommend(skills)

    return render_template(
        "vacancies.html",
        vacancies=recommendations
    )