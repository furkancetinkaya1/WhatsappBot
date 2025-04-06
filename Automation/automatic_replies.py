# Kullanıcı durumlarını takip etmek için
user_states = {}  # user_id -> state

# Örnek sipariş veritabanı (telefon ve e-posta eşleştirmesiyle)
siparis_veritabani = {
    "whatsapp:+905301449892": {"kargo": "Kargonuz yola çıktı ve dağıtım merkezinde."},
    "test@example.com": {"kargo": "Siparişiniz kargoya verildi, 2 gün içinde teslim edilecek."}
}

# Mesaj işleme fonksiyonu
kullanici_eposta_istegi = {}  # user_id -> True/False

def process_message(incoming_msg, user_id):
    global kullanici_eposta_istegi

    if user_id not in user_states:
        user_states[user_id] = "awaiting_selection"
        return (
            "Merhaba! Size nasıl yardımcı olabilirim?\n"
            "Lütfen bir seçenek belirtin:\n"
            "1. Mağaza Sitesine Git\n"
            "2. Kargo Takip\n"
            "3. Sıkça Sorulan Sorular"
        )

    if user_states[user_id] == "awaiting_selection":
        if "1" in incoming_msg or "mağaza" in incoming_msg:
            user_states.pop(user_id)
            return "Mağaza sitemize yönlendirmek için tıklayın: https://www.orneksite.com"
        elif "2" in incoming_msg or "kargo" in incoming_msg:
            user_states[user_id] = "tracking"
            # Kullanıcıdan önce telefonla kontrol edilecek
        elif "3" in incoming_msg or "soru" in incoming_msg:
            from FAQs.faq import faq_data
            user_states[user_id] = "faq_selection"
            numbered_faqs = "\n".join([f"{i+1}. {q}" for i, q in enumerate(faq_data.keys())])
            return f"Sıkça Sorulan Sorular:\n{numbered_faqs}\nLütfen bir seçenek girin (1, 2, 3, ...)."
        else:
            return "Lütfen geçerli bir seçenek girin: 1, 2 veya 3"

    if user_states.get(user_id) == "awaiting_email":
        email = incoming_msg.strip().lower()
        if email in siparis_veritabani:
            user_states.pop(user_id)
            return f"E-posta adresinizle eşleşen sipariş bulundu. {siparis_veritabani[email]['kargo']}"
        else:
            return "Üzgünüz, bu e-posta adresine ait sipariş bulunamadı. Lütfen kontrol edip tekrar deneyin."

    if user_states.get(user_id) == "tracking":
        if user_id in siparis_veritabani:
            user_states.pop(user_id)
            return f"Sistemde kayıtlı sipariş bulundu. {siparis_veritabani[user_id]['kargo']}"
        else:
            user_states[user_id] = "awaiting_email"
            return "Bu telefon numarasına kayıtlı sipariş bulunamadı. Sipariş verdiğiniz e-posta adresinizi yazar mısınız?"

    if user_states.get(user_id) == "faq_selection":
        try:
            from FAQs.faq import get_faq_answer, faq_data
            index = int(incoming_msg.strip()) - 1
            faq_list = list(faq_data.keys())
            if 0 <= index < len(faq_list):
                question = faq_list[index]
                answer = get_faq_answer(question)
                user_states.pop(user_id)
                return answer
            else:
                return "Lütfen listeden geçerli bir numara seçin."
        except (ValueError, IndexError):
            return "Lütfen sadece listedeki numaralardan birini girin."

    if user_states.get(user_id) == "faq_answer_selection":
        from FAQs.faq import get_faq_answer
        from FAQs.faq import faq_data
        faq_list = list(faq_data.keys())
        question = faq_list[int(incoming_msg.strip()) - 1]
        answer = get_faq_answer(question)
        user_states.pop(user_id)
        return answer

    return "Geçersiz mesaj."