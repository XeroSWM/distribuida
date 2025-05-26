from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"<h1>¡Despliegue automático con Flask funciona! 🚀</h1>" \
           f"<p>Última actualización: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
