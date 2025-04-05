import os
from flask import Flask, request, Response

app = Flask(__name__)

def save_user_name(user_id, user_name):
    """Kullanıcı adını dosyaya kaydet"""
    with open("user_data.txt", "a") as file:
        file.write(f"{user_id},{user_name}\n")

def get_user_name(user_id):
    """Kullanıcı adını dosyadan al"""
    if not os.path.exists("user_data.txt"):
        return None
    with open("user_data.txt", "r") as file:
        for line in file:
            stored_user_id, stored_user_name = line.strip().split(",")
            if stored_user_id == user_id:
                return stored_user_name
    return None

@app.route("/", methods=["GET"])
def home():
    return "Bot çalışıyor!"

product_prices = {
    "konut": "499 TL",
    "arsa": "350 TL",
    "işyeri": "1000 TL"
}

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    user_id = request.values.get('From', '')  # Kullanıcının telefon numarasını al

    print("Gelen mesaj:", incoming_msg)

    # Kullanıcı adını alma veya kaydetme
    user_name = get_user_name(user_id)
    reply = ""

    if "merhaba" in incoming_msg:
        if user_name:
            reply = f"Merhaba {user_name}! Size nasıl yardımcı olabilirim?"
        else:
            reply = "Merhaba! Adınızı öğrenebilir miyim?"
    elif "adım" in incoming_msg:
        user_name = incoming_msg.split("adım")[-1].strip()  # Kullanıcı adını al
        save_user_name(user_id, user_name)  # Adı kaydet
        reply = f"Adınızı kaydettim, {user_name}. Size nasıl yardımcı olabilirim?"
        if "fiyat" in incoming_msg:
            if "konut" in incoming_msg:
                reply = f"Konut fiyatımız {product_prices['konut']}."
            elif "arsa" in incoming_msg:
                reply = f"Arsa fiyatımız {product_prices['arsa']}."
            elif "işyeri" in incoming_msg:
                reply = f"İşyeri fiyatımız {product_prices['işyeri']}."
            else:
                reply = "Hangi ürün hakkında bilgi almak istersiniz? Konut, Arsa, İşyeri?"
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