from flask import Flask, request, send_file
from flask_cors import CORS  # Certifique-se de que flask_cors está instalado
from gtts import gTTS
import os

app = Flask(__name__)

# Habilita CORS apenas para a origem http://localhost:3001 em todas as rotas
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/synthesize', methods=['POST'])
def synthesize():
    try:
        # Obtém o JSON enviado na requisição
        data = request.json
        text = data.get("text", "")

        # Validação: retorna erro se o texto estiver ausente
        if not text:
            return {"error": "Texto ausente da requisição"}, 400

        # Gera o áudio utilizando o gTTS
        tts = gTTS(text=text, lang='pt')
        filename = "audio.mp3"
        tts.save(filename)

        # Envia o arquivo de áudio como resposta
        return send_file(filename, mimetype="audio/mpeg")

    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
