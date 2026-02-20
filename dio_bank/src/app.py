from flask import Flask, request

app = Flask(__name__)


@app.route("/olamundo/<usuario>/<int:idade>/<float:altura>")
def olamundo(usuario, idade, altura):
    return {
        "usuario": usuario,
        "idade": idade,
        "altura": altura,
    }


@app.route("/bemvindo")
def welcome():
    return {
        "message": "Bem-vindo ao DIO Bank!",
        "description": "Aqui você pode encontrar informações sobre nossos serviços e projetos.",
    }


@app.route("/projects")
def projects():
    return "Lista de projetos do DIO Bank!"


@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "POST":
        return "Informações sobre o DIO Bank (POST)"
    else:
        return "Informações sobre o DIO Bank (GET)"
