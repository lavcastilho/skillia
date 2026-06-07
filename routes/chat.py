from flask import Blueprint, render_template, request, jsonify

chat_bp = Blueprint("chat", __name__)

CHAT_MEMORY = []

@chat_bp.route("/chat")
def chat():

    return render_template("chat.html")


@chat_bp.route("/chat/message", methods=["POST"])
def message():

    user_msg = request.json.get("message")

    response = generate_response(user_msg)

    CHAT_MEMORY.append({
        "user": user_msg,
        "ski": response
    })

    return jsonify({
        "response": response
    })


def generate_response(msg):

    msg = msg.lower()

    if "vaga" in msg:
        return "Posso te ajudar a encontrar vagas compatíveis com seu perfil!"

    if "curriculo" in msg:
        return "Envie seu currículo para eu analisá-lo para você."

    if "curso" in msg:
        return "Recomendo cursos de Python, React e SQL para você evoluir!"

    return "Entendi. Estou aqui para te ajudar na sua jornada profissional!"