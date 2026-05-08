from flask import Flask, request, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder='static')

# ── Главная страница
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# ── Страница успеха
@app.route('/success')
def success():
    return send_from_directory('static', 'success.html')

# ── Страница состояния для Volet (Status URL)
@app.route('/status', methods=['GET', 'POST'])
def status():
    data = request.form if request.method == 'POST' else request.args
    print("=== VOLET PAYMENT ===")
    for key, value in data.items():
        print(f"{key}: {value}")
    print("=====================")
    return 'OK', 200

# ── Отдаём статические файлы (фото и др.)
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
