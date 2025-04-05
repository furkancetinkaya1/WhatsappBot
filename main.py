from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot çalışıyor!"

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    # Kullanıcıdan gelen mesajı al
    incoming_msg = request.values.get('Body', '').strip().lower()
    print("Gelen mesaj:", incoming_msg)

    # Yanıt mesajını başlat
    reply = ""

    # Komutlara göre yanıtları belirle
    if "merhaba" in incoming_msg:
        reply = "Merhaba! Size nasıl yardımcı olabilirim? Eğer yardım almak isterseniz 'yardım' yazabilirsiniz."
    elif "yardım" in incoming_msg:
        reply = ("Botun komutları:\n"
                 "- 'merhaba' : Hoş geldiniz mesajı\n"
                 "- 'fiyat' : Ürün fiyat bilgisi\n"
                 "- 'kargo' : Kargo süresi\n"
                 "- 'menü' : Mevcut seçenekleri gör\n"
                 "- 'yardım' : Bot komutlarını öğren\n"
                 "Yardım almak için yukarıdaki komutlardan birini yazabilirsiniz.")
    elif "fiyat" in incoming_msg:
        reply = "Ürün fiyatımız 499 TL'dir."
    elif "kargo" in incoming_msg:
        reply = "Kargo süremiz 1-3 iş günüdür."
    elif "menü" in incoming_msg:
        reply = ("Mevcut seçenekler:\n"
                 "- Fiyat bilgisi almak için 'fiyat' yazın\n"
                 "- Kargo süresi öğrenmek için 'kargo' yazın\n"
                 "- Yardım almak için 'yardım' yazın")
    else:
        reply = "Maalesef sizi anlayamadım. Yardım almak için 'yardım' yazabilirsiniz."

    # Twilio'dan mesaj yanıtı oluştur
    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)