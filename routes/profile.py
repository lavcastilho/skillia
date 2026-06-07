from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from flask_login import (
    login_required,
    current_user
)

from models.db import db
from models.profile import Profile

profile_bp = Blueprint(
    "profile",
    __name__
)

@profile_bp.route("/profile")
@login_required
def profile():

    user_profile = Profile.query.filter_by(
        user_id=current_user.id
    ).first()

    return render_template(
        "profile.html",
        profile=user_profile
    )

@profile_bp.route(
    "/profile/save",
    methods=["POST"]
)
@login_required
def save_profile():

    education = request.form.get(
        "education"
    )

    experience = request.form.get(
        "experience"
    )

    skills = request.form.get(
        "skills"
    )

    profile = Profile.query.filter_by(
        user_id=current_user.id
    ).first()

    if not profile:

        profile = Profile(
            user_id=current_user.id
        )

        db.session.add(profile)

    profile.education = education
    profile.experience = experience
    profile.skills = skills

    db.session.commit()

    return redirect("/profile")