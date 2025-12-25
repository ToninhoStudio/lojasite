from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Coloca aqui o webhook do teu Discord
DISCORD_WEBHOOK = "COLOCA_AQUI_O_WEBHOOK_DO_DISCORD"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/comprar", methods=["POST"])
def comprar():
    produto = request.form["produto"]
    preco = request.form["preco"]

    requests.post(DISCORD_WEBHOOK, json={
        "content": f"🛒 Nova compra no SITE\nProduto: {produto}\nPreço: {preco}"
    })

    return "✅ Pedido enviado! O admin vai contactar-te no Discord."

app.run(host="0.0.0.0", port=10000)
