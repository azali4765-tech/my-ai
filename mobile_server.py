"""Mobile سے Commands بھیجنے کے لیے سرور
اپنے phone پر یہ کھولیں: http://LAPTOP_IP:5000
"""

from flask import Flask, request, jsonify
from jarvis_core import handle_command, speak

app = Flask(__name__)

print("\n" + "="*50)
print("📱 Mobile Server شروع ہو رہا ہے...")
print("="*50)
print("\n📍 اپنے phone پر یہ address کھولیں:")
print("http://192.168.x.x:5000")
print("(اپنا laptop IP address ڈالیں)\n")


@app.route('/', methods=['GET'])
def home():
    """صرف HTML صفحہ دکھائے"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Jarvis - Mobile Control</title>
        <style>
            body { font-family: Arial; text-align: center; padding: 20px; background: #1a1a1a; color: white; }
            h1 { color: #00ff00; }
            input { width: 80%; padding: 10px; font-size: 16px; border: 2px solid #00ff00; border-radius: 5px; }
            button { width: 85%; padding: 10px; margin-top: 10px; font-size: 16px; background: #00ff00; color: black; border: none; border-radius: 5px; cursor: pointer; }
            button:hover { background: #00cc00; }
            #response { margin-top: 20px; padding: 10px; background: #333; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>🤖 JARVIS</h1>
        <p>آپ کا Personal Assistant</p>
        <input type="text" id="cmd" placeholder="Command لکھیں... مثلاً: open notepad" />
        <br>
        <button onclick="sendCommand()">بھیجیں</button>
        <div id="response"></div>
        
        <script>
            function sendCommand() {
                let cmd = document.getElementById('cmd').value;
                if (!cmd) return;
                
                fetch('/api/command', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({command: cmd})
                })
                .then(r => r.json())
                .then(data => {
                    document.getElementById('response').innerHTML = '<strong>Jarvis:</strong> ' + data.response;
                    document.getElementById('cmd').value = '';
                });
            }
            
            document.getElementById('cmd').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') sendCommand();
            });
        </script>
    </body>
    </html>
    """
    return html


@app.route('/api/command', methods=['POST'])
def api_command():
    """Phone سے command لینا"""
    data = request.get_json() or {}
    command = data.get('command', '').strip()
    
    if not command:
        return jsonify({'error': 'کوئی command نہیں'}), 400
    
    print(f"📱 Mobile سے: {command}")
    response = handle_command(command)
    
    try:
        speak(response)
    except:
        pass
    
    return jsonify({
        'command': command,
        'response': response,
        'status': 'ok'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
