from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot çalışıyor!"

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    print("Gelen mesaj:", incoming_msg)
    return "Mesaj alındı", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Bu satırda port ve host'u belirt