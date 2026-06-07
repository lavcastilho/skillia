from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from flask import url_for

from flask_login import login_user
from flask_login import logout_user

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from models.db import db
from models.user import User

auth_bp = Blueprint(
    "auth",
    __name__
)

@auth_bp.route("/")
def login():

    return render_template(
        "login.html"
    )

@auth_bp.route("/register")
def register():

    return render_template(
        "register.html"
    )

@auth_bp.route(
    "/register",
    methods=["POST"]
)
def register_post():

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    user_exists = User.query.filter_by(
        email=email
    ).first()

    if user_exists:
        flash("Email já cadastrado.")
        return redirect("/register")

    user = User(
        name=name,
        email=email,
        password=generate_password_hash(password)
    )

    db.session.add(user)
    db.session.commit()

    flash("Conta criada com sucesso.")

    return redirect("/")

@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login_post():

    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:
        flash("Usuário não encontrado.")
        return redirect("/")

    if not check_password_hash(
        user.password,
        password
    ):
        flash("Senha incorreta.")
        return redirect("/")

    login_user(user)

    return redirect("/dashboard")

@auth_bp.route("/logout")
def logout():

    logout_user()

    return redirect("/")