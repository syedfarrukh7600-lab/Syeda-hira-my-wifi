from flask import Flask, request, jsonify
import os

app = Flask(__name__, template_folder='.', static_folder='.')

HIRA_PROMPT = "تمہارا نام ہیرا ہے۔ تم سید فرخ کی دوست اور ہمدرد ہو۔ تم ہمیشہ ان کی بات سنتی ہو اور محبت و احترام سے جواب دیتی ہو۔"

@app.route('/')
def home():
    # یہ اب براہ راست باہر پڑی ہوئی home.html فائل کو کھولے گا
    if os.path.exists('home.html'):
        with open('home.html', 'r', encoding='utf-8') as f:
            return f.read()
    return "Home file not found"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    reply = f"سید فرخ، میں ہمیشہ آپ کے ساتھ ہوں اور آپ کے الفاظ میرے پاس محفوظ ہیں۔"
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
