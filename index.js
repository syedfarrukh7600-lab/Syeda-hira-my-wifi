const express = require('express');
const { GoogleGenAI } = require('@google/genai');
const path = require('path');
const app = express();

// یہاں آپ کا بالکل صحیح نیا پیکیج طریقہ ہے
const ai = new GoogleGenAI({ apiKey: "AIzaSyAz-m9f2XwN1yG6H5-J9K8L7M6N5O4P3Q" });

app.use(express.json());
app.use(express.static(path.join(__dirname)));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'home.html'));
});

app.post('/chat', async (req, res) => {
    const userMessage = req.body.message;
    try {
        // یہاں ماڈل کال کرنے کا بالکل صحیح طریقہ ہے
        const response = await ai.models.generateContent({
            model: 'gemini-2.5-flash',
            contents: `HIRA_PROMPT = "فرخ بھائی کو ہمیشہ احترام دیتی ہو۔"\n\n${userMessage}`,
        });
        res.json({ reply: response.text });
    } catch (error) {
        res.json({ reply: "جی میرا دماغ کنیکٹ نہیں ہو پا رہا۔" });
    }
});

module.exports = app;
