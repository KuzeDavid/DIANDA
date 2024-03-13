from flask import Flask, request, jsonify

app = Flask(__name__)

# Middleware para manejar las cabeceras CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route("/", methods=["GET", "POST"])
def recibir_respuestas():
    if request.method == "POST":
        # Obtiene las respuestas del formulario
        respuestas = request.get_json()

        # Procesa las respuestas con machine learning
        print(respuestas)

        # Devuelve las respuestas en formato JSON
        return jsonify(respuestas)
    else:
        return "ML Funcionando!"

if __name__ == "__main__":
    app.run()
