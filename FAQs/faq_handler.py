from FAQs.faq import get_faq_list, get_faq_answer

def handle_faq_request(user_message):
    # Eğer kullanıcı 'Sıkça Sorulan Sorular' seçtiyse
    if user_message == "3":
        # Sıkça Sorulan Sorular listesini gönderiyoruz
        faqs = get_faq_list()
        faq_message = "Sıkça Sorulan Sorular:\n"
        for idx, faq in enumerate(faqs, start=1):
            faq_message += f"{idx}. {faq}\n"
        faq_message += "Lütfen bir seçenek girin (1, 2, 3, ...)."
        return faq_message

    # Eğer kullanıcı numara girerse, cevabı alır
    elif user_message.isdigit() and int(user_message) in range(1, 7):
        question = get_faq_list()[int(user_message) - 1]
        answer = get_faq_answer(question)
        return answer
    else:
        return "Geçerli bir seçenek giriniz (1, 2, 3, ...)."