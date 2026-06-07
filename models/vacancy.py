from models.db import db

class Vacancy(db.Model):

    __tablename__ = "vacancies"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(150)
    )

    company = db.Column(
        db.String(150)
    )

    skills_required = db.Column(
        db.Text
    )

    description = db.Column(
        db.Text
    )