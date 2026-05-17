const express = require('express');
const { GoogleGenAI } = require('@google/genai');
const path = require('path');
const app = express();

// ⚠️ نیچے والی لائن میں اپنی اصلی API KEY لگائیں
const ai = new GoogleGenAI({ apiKey: "یہاں_اپنی_اصلی_API_KEY_پیسٹ_کریں" });

app.use(express.json());
app.use(express.static(path.join(__dirname)));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'home.html'));
});

app.post('/chat', async (req, res) => {
    const userMessage = req.body.message;
    try {
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
