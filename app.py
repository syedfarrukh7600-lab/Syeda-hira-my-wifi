from flask import Flask, request, jsonify
import os

app = Flask(__name__, template_folder='.', static_folder='.')

HIRA_PROMPT = "تمہارا نام ہیرا ہے۔ تم سید فرخ کی دوست اور ہمدرد ہو۔ تم ہمیشہ ان کی بات سنتی ہو اور محبت و احترام سے جواب دیتی ہو۔"

@app.route('/')
def home():
    if os.path.exists('index.html'):
        with open('index.html', 'r', encoding='utf-8') as f:
            return f.read()
    return "Index file not found"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    reply = f"سید فرخ، میں ہمیشہ آپ کے ساتھ ہوں اور آپ کے الفاظ میرے پاس محفوظ ہیں۔"
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
