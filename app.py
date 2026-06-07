print("Arquivo iniciou")

from flask import Flask, render_template
from flask_login import LoginManager

from config import Config
from models import db, User

from routes.profile import profile_bp
from routes.vacancies import vacancies_bp
from routes.chat import chat_bp
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp


# 1. CRIA APP PRIMEIRO
app = Flask(__name__)

# 2. CONFIG
app.config.from_object(Config)

# 3. DB
db.init_app(app)

# 4. LOGIN MANAGER
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# 5. ROTAS DIRETAS
@app.route("/home")
def home():
    return render_template("index.html")


# 6. BLUEPRINTS
app.register_blueprint(chat_bp)
app.register_blueprint(vacancies_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)


# 7. DB CREATE
with app.app_context():
    db.create_all()


# 8. RUN
if __name__ == "__main__":
    app.run(debug=True)