import os

class Config:
    SECRET_KEY = "skillia_secret_key_2026"

    SQLALCHEMY_DATABASE_URI = "sqlite:///skillia.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.path.join(
        "static",
        "uploads"
    )