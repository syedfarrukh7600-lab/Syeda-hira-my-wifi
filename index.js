const express = require('express');
const path = require('path');
const { GoogleGenAI } = require('@google/genai');

const app = express();
app.use(express.json());

// API Key کو ورسیل کے انوائرمنٹ سے اٹھانا
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// ۱. جب کوئی ویب سائٹ کھولے تو home.html سامنے آئے
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'home.html'));
});

// ۲. ہیرا کے ساتھ چیٹ کرنے کا مین راستہ
app.post('/api/chat', async (req, res) => {
    try {
        const { message } = req.body;
        
        const response = await ai.models.generateContent({
            model: 'gemini-2.5-flash',
            contents: message
        });
        
        res.json({ reply: response.text });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// ورسیل کے لیے ایکسپورٹ
module.exports = app;
