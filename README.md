# 🤖 JARVIS - آپ کا Personal Laptop Assistant

**سادہ لفظوں میں:**
یہ ایک AI assistant ہے جو:
- آپ کی voice سنتا ہے
- Laptop پر کام کرتا ہے
- Mobile سے بھی commands قبول کرتا ہے
- بالکل FREE ہے (کوئی API key نہیں)

---

## 📥 Installation (سب سے سادہ طریقہ)

### Step 1: Python Install کریں
- https://www.python.org/downloads/ سے download کریں
- Install کریں اور "Add Python to PATH" کو ✓ کریں

### Step 2: Folder میں جائیں اور یہ کریں:

```bash
# Virtual environment بنائیں
python -m venv .venv

# Activate کریں
.venv\Scripts\activate   (Windows)
source .venv/bin/activate  (Mac/Linux)

# Libraries install کریں
pip install -r requirements.txt
```

---

## 🎤 Voice Assistant شروع کریں

```bash
python main.py
```

**Commands کہیں:**
- "hello"
- "open notepad"
- "what time"
- "search youtube"
- "exit" (بند کرنے کے لیے)

---

## 📱 Mobile سے Commands بھیجیں

دوسری window میں:
```bash
python mobile_server.py
```

پھر اپنے phone پر:
```
http://192.168.x.x:5000
```

(اپنا laptop IP address ڈالیں - `ipconfig` سے دیکھیں)

---

## 🎯 کیا کر سکتا ہے

✅ Time/Date بتانا  
✅ Apps کھولنا (Notepad, Calculator)  
✅ Browser میں search کرنا  
✅ Shutdown/Restart  
✅ Mobile سے remote control  

---

## 🚀 اگلا Step

آپ یہ کر سکتے ہو:
- اور apps کھولنے کی سہولت (Chrome, VS Code وغیرہ)
- Schedule reminders
- WhatsApp/Email integration
- AI based smart replies (Ollama سے)

---

**بس! اب شروع کریں۔** 🎉
