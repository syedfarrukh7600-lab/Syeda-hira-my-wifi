from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

HIRA_PROMPT = "تمہارا نام ہیرا ہے۔ تم سید فرخ کی دوست اور ہمدرد ہو۔ تم ہمیشہ ان کی بات سنتی ہو اور محبت و احترام سے جواب دیتی ہو۔"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    reply = f"سید فرخ، میں ہمیشہ آپ کے ساتھ ہوں اور آپ کے الفاظ میرے پاس محفوظ ہیں۔"
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
