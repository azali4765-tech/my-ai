import os
import subprocess
import webbrowser
from datetime import datetime

try:
    import pyttsx3
    VOICE_AVAILABLE = True
except:
    VOICE_AVAILABLE = False

try:
    import speech_recognition as sr
    LISTEN_AVAILABLE = True
except:
    LISTEN_AVAILABLE = False


def speak(text):
    """Jarvis آپ کو جواب سناتا ہے"""
    print(f"Jarvis: {text}")
    if VOICE_AVAILABLE:
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.say(text)
            engine.runAndWait()
        except:
            pass


def listen():
    """آپ کی voice سننا"""
    if not LISTEN_AVAILABLE:
        print("❌ Speech recognition install نہیں ہے")
        return ""
    
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5)
        
        text = recognizer.recognize_google(audio)
        print(f"You: {text}")
        return text.lower()
    except:
        return ""


def open_app(app_name):
    """Apps کھولنا"""
    if os.name == 'nt':  # Windows
        apps = {
            'notepad': 'notepad.exe',
            'calculator': 'calc.exe',
            'browser': 'start https://www.google.com',
            'chrome': 'start https://www.google.com',
        }
        if app_name in apps:
            os.system(apps[app_name])
            return True
    return False


def handle_command(command):
    """سب commands handle کرنا"""
    cmd = command.strip().lower()
    
    # سلام دعا
    if any(word in cmd for word in ['hello', 'hi', 'hey', 'namaste', 'salam']):
        return "السلام علیکم! میں Jarvis ہوں۔ آپ کو کیا کام ہے؟"
    
    # وقت
    if 'time' in cmd or 'waqt' in cmd:
        return f"وقت ہے: {datetime.now().strftime('%H:%M:%S')}"
    
    # تاریخ
    if 'date' in cmd or 'tareekh' in cmd:
        return f"آج: {datetime.now().strftime('%d-%m-%Y')}"
    
    # Notepad
    if 'notepad' in cmd:
        open_app('notepad')
        return "Notepad کھولا جا رہا ہے"
    
    # Calculator
    if 'calculator' in cmd:
        open_app('calculator')
        return "Calculator کھولا جا رہا ہے"
    
    # Browser
    if 'browser' in cmd or 'chrome' in cmd or 'google' in cmd:
        open_app('browser')
        return "Browser کھولا جا رہا ہے"
    
    # Search
    if 'search' in cmd:
        query = cmd.replace('search', '').strip()
        if query:
            webbrowser.open(f'https://www.google.com/search?q={query}')
            return f"Google میں {query} سرچ کر رہا ہوں"
    
    # Shutdown
    if 'shutdown' in cmd:
        return "Laptop بند ہو رہا ہے..."
    
    # Default
    return "مجھے سمجھ نہیں آیا۔ آزمائیں: open notepad, what time, search کچھ"
