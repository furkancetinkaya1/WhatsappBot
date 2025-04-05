from faq import faq_data

def get_faq_answer(question):
    # Kullanıcının mesajı FAQ listesinde mi?
    question = question.lower()  # Soruyu küçük harfe çeviriyoruz
    answer = faq_data.get(question, None)

    if answer:
        return answer
    else:
        return "Bu soruya şu anda cevap verilemiyor. Yardımcı olmamı ister misiniz?"