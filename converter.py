from flask import Flask, request, sendfile
from flaskcors import CORS
from gtts import gTTS
import os

app = Flask(name)
CORS(app)  # Enables CORS for all routes and methods

@app.route('/synthesize', methods=['POST'])
def synthesize():
    try:
        # Obtém o texto enviado na requisição
        data = request.json
        text = data.get("text", "")

        # Validação simples
        if not text:
            return {"error": "Texto ausente da requisição"}, 400

        # Gera o áudio usando gTTS
        tts = gTTS(text=text, lang='pt')
        filename = "audio.mp3"
        tts.save(filename)

        # Envia o arquivo de áudio como resposta
        return sendfile(filename, mimetype="audio/mpeg")

    except Exception as e:
        return {"error": str(e)}, 500

if _name == '__main':
    app.run(host='0.0.0.0', port=5000)