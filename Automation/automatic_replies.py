import os

# Örnek sipariş veritabanı (telefon ve e-posta eşleştirmesiyle)
siparis_veritabani = {
    "whatsapp:+905551112233": {"kargo": "Kargonuz yola çıktı ve dağıtım merkezinde."},
    "test@example.com": {"kargo": "Siparişiniz kargoya verildi, 2 gün içinde teslim edilecek."}
}

# Mesaj işleme fonksiyonu
kullanici_eposta_istegi = {}  # user_id -> True/False

def process_message(incoming_msg, user_id):
    global kullanici_eposta_istegi

    # Eğer kullanıcıdan e-posta bekleniyorsa
    if kullanici_eposta_istegi.get(user_id, False):
        email = incoming_msg.strip().lower()
        if email in siparis_veritabani:
            kargo_durumu = siparis_veritabani[email]["kargo"]
            reply = f"E-posta adresinizle eşleşen sipariş bulundu. {kargo_durumu}"
        else:
            reply = "Üzgünüz, bu e-posta adresine ait sipariş bulunamadı. Lütfen kontrol edip tekrar deneyin."
        kullanici_eposta_istegi[user_id] = False
        return reply

    # Öncelikle telefon numarasına göre sipariş kontrolü
    if user_id in siparis_veritabani:
        kargo_durumu = siparis_veritabani[user_id]["kargo"]
        reply = f"Sistemde kayıtlı sipariş bulundu. {kargo_durumu}"
    else:
        reply = "Bu telefon numarasına kayıtlı bir sipariş bulunamadı. Sipariş verdiğiniz e-posta adresinizi yazar mısınız?"
        kullanici_eposta_istegi[user_id] = True

    return reply