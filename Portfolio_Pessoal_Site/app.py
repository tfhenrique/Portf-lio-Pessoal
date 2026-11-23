from flask import Flask, jsonify, render_template

app = Flask(__name__)

PROJECTOS = [
    {
        "id": 1,
        "titulo": "Gestor de Tarefas em Python",
        "resumo": "Aplicação em linha de comandos e web simples para organizar tarefas diárias e prioridades.",
        "descricao": "Desenvolvi este projeto para praticar estruturas de dados, funções e organização modular em Python. Permite criar, concluir e filtrar tarefas.",
        "tecnologias": ["Python", "HTML", "CSS"],
        "ano": 2025,
    },
    {
        "id": 2,
        "titulo": "Landing Page Responsiva para Estúdio Criativo",
        "resumo": "Página promocional adaptada a desktop e mobile com foco em tipografia e layout limpo.",
        "descricao": "Projeto focado em CSS moderno, flexbox/grid e media queries para garantir boa leitura em ecrãs pequenos e grandes.",
        "tecnologias": ["HTML5", "CSS3", "Flask"],
        "ano": 2025,
    },
    {
        "id": 3,
        "titulo": "API Simples de Catálogo",
        "resumo": "Endpoint JSON para expor dados estruturados consumidos por outras aplicações.",
        "descricao": "Implementação de rotas REST básicas em Flask com serialização JSON para testar integração entre backend e frontend.",
        "tecnologias": ["Python", "Flask", "JSON"],
        "ano": 2026,
    },
]

@app.route("/")
def index():
    return render_template("index.html", projectos=PROJECTOS[:2])


@app.route("/sobre")
def sobre():
    competencias = [
        "Python & Flask",
        "HTML5 & CSS3 (Media Queries)",
        "Git & GitHub",
        "Resolução de problemas",
    ]
    return render_template("about.html", competencias=competencias)


@app.route("/projectos")
def projectos():
    return render_template("projects.html", projectos=PROJECTOS)


@app.route("/projecto/<int:id>")
def detalhe_projecto(id):
    projecto = next((p for p in PROJECTOS if p["id"] == id), None)
    if projecto is None:
        return render_template("404.html"), 404
    return render_template("project_details.html", projecto=projecto)


@app.route("/api/projectos")
def api_projectos():
    return jsonify(PROJECTOS)


@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)