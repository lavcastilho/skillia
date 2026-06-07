from models.db import db


class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    education = db.Column(db.Text)
    experience = db.Column(db.Text)
    skills = db.Column(db.Text)

    resume_file = db.Column(db.String(255))
    detected_skills = db.Column(db.Text)