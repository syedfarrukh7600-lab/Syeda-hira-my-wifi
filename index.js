const express = require('express');
const path = require('path');
const { GoogleGenAI } = require('@google/genai');

const app = express();
app.use(express.json());

// API Key کو ورسیل کے انوائرمنٹ ویری ایبل سے اٹھانا
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// ۱. جب کوئی آپ کی ویب سائٹ کھولے تو home.html شو ہو جائے (اس سے 404 ایرر ختم ہوگا)
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'home.html'));
});

// ۲. ہیرا کے ساتھ چیٹ کرنے کا بیک اینڈ روٹ
app.post('/api/chat', async (req, res) => {
    try {
        const { message } = req.body;
        
        // جمنائی ماڈل کو کال کرنا
        const response = await ai.models.generateContent({
            model: 'gemini-2.5-flash',
            contents: message
        });
        
        res.json({ reply: response.text });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// ورسیل کے لیے سرور ایکسپورٹ کرنا
module.exports = app;
