# Automation/nlp_helper.py

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

faq_prompts = {
    "kargo nerede": "Kargonuzun nerede olduğunu öğrenmek istiyorsanız...",
    "iade nasıl yapılır": "İade işlemleri için...",
    "ödeme seçenekleri": "Ödeme yöntemlerimiz şunlardır...",
    "ürün fiyatı": "Ürün fiyatlarımız model ve kategoriye göre değişir...",
    "ürünler hakkında bilgi": "Çeşitli elektronik ürünler sunuyoruz...",
}

def get_semantic_answer(user_message):
    prompt = "Aşağıda bir müşteri mesajı yer alıyor. Bu mesaj en çok hangi önceden tanımlı soruya benziyor?\n\n"
    prompt += f"Kullanıcı mesajı: {user_message}\n"
    prompt += "Ön tanımlı sorular:\n"

    for i, key in enumerate(faq_prompts.keys(), 1):
        prompt += f"{i}. {key}\n"

    prompt += "Cevap olarak sadece en yakın eşleşen sorunun numarasını ver.\n"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    reply = response["choices"][0]["message"]["content"].strip()

    try:
        matched_index = int(reply) - 1
        matched_key = list(faq_prompts.keys())[matched_index]
        return faq_prompts[matched_key]
    except:
        return "Mesajınızı anlayamadım. Daha net ifade edebilir misiniz?"