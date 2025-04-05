import os
from flask import Flask, request, Response
from home_view import home_page
from contact_page import contact_page
from about_page import about_page

app = Flask(__name__)

# Kullanıcı adı kaydetme fonksiyonu
def save_user_name(user_id, user_name):
    """Kullanıcı adını dosyaya kaydet"""
    try:
        with open("user_data.txt", "a") as file:
            file.write(f"{user_id},{user_name}\n")
    except Exception as e:
        print(f"Dosyaya kaydetme hatası: {e}")


# Kullanıcı adını dosyadan alma fonksiyonu
def get_user_name(user_id):
    """Kullanıcı adını dosyadan al"""
    try:
        if not os.path.exists("user_data.txt"):
            return None
        with open("user_data.txt", "r") as file:
            for line in file:
                stored_user_id, stored_user_name = line.strip().split(",")
                if stored_user_id == user_id:
                    return stored_user_name
        return None
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return None


# Ürün fiyatları
product_prices = {
    "konut": "499 TL",
    "arsa": "350 TL",
    "işyeri": "1000 TL"
}


# Mesaj işleme fonksiyonu
def process_message(incoming_msg, user_id):
    """Gelen mesajı işleyip yanıt döndüren fonksiyon"""
    user_name = get_user_name(user_id)

    if "merhaba" in incoming_msg:
        reply = f"Merhaba {user_name if user_name else 'misafir'}! Size nasıl yardımcı olabilirim?"
    elif "adım" in incoming_msg:
        user_name = incoming_msg.split("adım")[-1].strip()
        save_user_name(user_id, user_name)
        reply = f"Adınızı kaydettim, {user_name}. Size nasıl yardımcı olabilirim?"
    elif "fiyat" in incoming_msg:
        reply = get_price_response(incoming_msg)
    elif "kargo" in incoming_msg:
        reply = "Kargo süremiz 1-3 iş günüdür."
    else:
        reply = "Maalesef sizi anlayamadım. Daha detaylı yazar mısınız?"

    return reply


# Fiyatlarla ilgili yanıt veren fonksiyon
def get_price_response(message):
    """Fiyatla ilgili gelen mesajı işleyip yanıt döndüren fonksiyon"""
    if "konut" in message:
        return f"Konut fiyatımız {product_prices['konut']}."
    elif "arsa" in message:
        return f"Arsa fiyatımız {product_prices['arsa']}."
    elif "işyeri" in message:
        return f"İşyeri fiyatımız {product_prices['işyeri']}."
    else:
        return "Hangi ürün hakkında bilgi almak istersiniz? Konut, Arsa, İşyeri?"


# Ana sayfa route'u
@app.route("/", methods=["GET"])
def home():
    return home_page()


# WhatsApp mesajı alıp yanıt döndüren route
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    user_id = request.values.get('From', '')  # Kullanıcının telefon numarasını al
    print("Gelen mesaj:", incoming_msg)

    # Mesajı işle ve yanıt al
    reply = process_message(incoming_msg, user_id)

    # XML yanıtını oluştur
    response = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{reply}</Message>
</Response>"""
    return Response(response, mimetype="application/xml")

@app.route("/iletisim", methods=["GET"])
def iletisim():
    return contact_page()

@app.route("/hakkimizda", methods=["GET"])
def hakkimizda():
    return about_page()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)