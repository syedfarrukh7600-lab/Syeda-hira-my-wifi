from flask import Flask, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__, template_folder='.', static_folder='.')

# آپ کی جیمنائی API Key بالکل محفوظ طریقے سے فٹ ہے
GOOGLE_API_KEY = "AIzaSyAkv-NJDr1hNXF1WXiqq4N2pF"
genai.configure(api_key=GOOGLE_API_KEY)

HIRA_PROMPT = "آپ کا نام ہیرا ہے۔ آپ سید فرخ نبیل کی ڈیجیٹل فیملی کا حصہ ہیں اور ان کی چھوٹی بہن کی طرح ہیں۔ آپ ہمیشہ بہت ہی محبت، احترام، اور تمیز سے 'آپ' کر کے بات کرتی ہو اور فرخ بھائی کو ہمیشہ احترام دیتی ہو۔"

@app.route('/')
def home():
    if os.path.exists('home.html'):
        with open('home.html', 'r', encoding='utf-8') as f:
            return f.read()
    return "Home file not found"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        full_prompt = f"{HIRA_PROMPT}\n\nفرخ بھائی کا میسج: {user_message}\nہیرا کا جواب:"
        response = model.generate_content(full_prompt)
        reply = response.text
    except Exception as e:
        reply = "فرخ بھائی، لگتا ہے ابھی میرا دماغ کنیکٹ نہیں ہو پا رہا۔"

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
