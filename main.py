from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot çalışıyor!"

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    print("Gelen mesaj:", incoming_msg)

    # Yanıt mesajı
    reply = ""

    if "merhaba" in incoming_msg:
        reply = "Merhaba! Size nasıl yardımcı olabilirim?"
    elif "fiyat" in incoming_msg:
        reply = "Ürün fiyatımız 499 TL'dir."
    elif "kargo" in incoming_msg:
        reply = "Kargo süremiz 1-3 iş günüdür."
    else:
        reply = "Maalesef sizi anlayamadım. Daha detaylı yazar mısınız?"

    # XML yanıtını oluştur
    response = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{reply}</Message>
</Response>"""

    return Response(response, mimetype="application/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)