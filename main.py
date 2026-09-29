"""JARVIS - Voice Assistant
یہ آپ کی voice سنتا ہے اور کام کرتا ہے
"""

from jarvis_core import listen, handle_command, speak

print("="*50)
print("🤖 JARVIS - آپ کا Personal Assistant")
print("="*50)
print("\n💡 Commands کریں:")
print("  - 'hello' / 'hi'")
print("  - 'what time' / 'what date'")
print("  - 'open notepad' / 'open calculator'")
print("  - 'search کچھ'")
print("  - 'exit' بند کرنے کے لیے")
print("\n")

while True:
    print("\n🎤 آپ کہیں...")
    command = listen()
    
    if not command:
        speak("سمجھ نہیں آیا")
        continue
    
    if 'exit' in command or 'quit' in command:
        speak("خدا حافظ!")
        break
    
    response = handle_command(command)
    speak(response)
