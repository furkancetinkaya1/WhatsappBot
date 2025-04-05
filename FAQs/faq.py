faq_data = {
    "botun çalışma durumu nedir?": "Botumuz şu anda aktif ve size yardımcı olmaya hazır!",
    "hangi ürünleri satıyorsunuz?": "Çeşitli elektronik ürünler, telefonlar, bilgisayarlar ve aksesuarlar satıyoruz.",
    "ürünlerin fiyatları nasıl?": "Ürünlerin fiyatları, model ve özelliklerine göre değişmektedir. Detaylı fiyat bilgisi için ürün sayfasını ziyaret edebilirsiniz.",
    "nasıl sipariş verebilirim?": "Ürünleri sepete ekleyebilir ve ödeme işlemini gerçekleştirebilirsiniz. Yardıma ihtiyacınız varsa canlı destek ile iletişime geçebilirsiniz.",
    "ödeme yöntemleriniz nelerdir?": "Kredi kartı, banka kartı ve kapıda ödeme gibi çeşitli ödeme seçeneklerimiz bulunmaktadır.",
    "iade koşulları nedir?": "Ürünlerimizde iade politikası mevcuttur. 14 gün içinde iade işlemini başlatabilirsiniz.",
}

def get_faq_list():
    return [
        "Botun çalışma durumu nedir?",
        "Hangi ürünleri satıyorsunuz?",
        "Ürünlerin fiyatları nasıl?",
        "Nasıl sipariş verebilirim?",
        "Ödeme yöntemleriniz nelerdir?",
        "İade koşulları nedir?"
    ]

def get_faq_answer(question):
    # Sorunun cevabını faq_data'dan alıyoruz
    question = question.strip().lower()  # Başındaki ve sonundaki boşlukları temizle ve küçük harfe çevir
    answer = faq_data.get(question, None)

    if answer:
        return answer
    else:
        return "Bu soruya şu anda cevap verilemiyor. Yardımcı olmamı ister misiniz?"