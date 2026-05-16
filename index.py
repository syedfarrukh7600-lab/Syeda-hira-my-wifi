from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="ur">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Syeda Hira - My WiFi</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #71b7e6, #9b59b6);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
                color: #fff;
            }
            .container {
                text-align: center;
                background: rgba(255, 255, 255, 0.15);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.18);
                max-width: 400px;
                width: 90%;
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            }
            p {
                font-size: 1.2rem;
                margin-bottom: 30px;
                opacity: 0.9;
            }
            .welcome-msg {
                font-size: 1.5rem;
                font-weight: bold;
                background: #fff;
                color: #9b59b6;
                padding: 15px 25px;
                border-radius: 50px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                display: inline-block;
                animation: pulse 2s infinite;
            }
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.05); }
                100% { transform: scale(1); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>سیدہ ہیرا</h1>
            <p>مائی وائی فائی نیٹ ورک میں خوش آمدید</p>
            <div class="welcome-msg">خوش آمدید! ✨</div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
