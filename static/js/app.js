async function sendMessage() {

    let input = document.getElementById("msg");
    let message = input.value;

    if (!message) return;

    addMessage("Você", message);

    input.value = "";

    const response = await fetch("/chat/message", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    });

    const data = await response.json();

    addMessage("SKI", data.response);
}

function addMessage(sender, text) {

    let box = document.getElementById("chat-box");

    let div = document.createElement("div");

    div.className = sender === "SKI" ? "msg ski" : "msg user";

    div.innerHTML = `<b>${sender}:</b> ${text}`;

    box.appendChild(div);

    box.scrollTop = box.scrollHeight;
}