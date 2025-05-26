from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    with open("index.html", "r", encoding="utf-8") as file:
        html = file.read()

    # Insertar la fecha en una marca personalizada {{last_update}}
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    html = html.replace("{{last_update}}", now)

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
