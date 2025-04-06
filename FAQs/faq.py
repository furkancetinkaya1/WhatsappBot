faq_data = {
    "Botun çalışma durumu nedir?": "Botumuz şu anda aktif ve size yardımcı olmaya hazır!",
    "Hangi ürünleri satıyorsunuz?": "Çeşitli elektronik ürünler, telefonlar, bilgisayarlar ve aksesuarlar satıyoruz.",
    "Ürünlerin fiyatları nasıl?": "Ürünlerin fiyatları, model ve özelliklerine göre değişmektedir. Detaylı fiyat bilgisi için ürün sayfasını ziyaret edebilirsiniz.",
    "Nasıl sipariş verebilirim?": "Ürünleri sepete ekleyebilir ve ödeme işlemini gerçekleştirebilirsiniz. Yardıma ihtiyacınız varsa canlı destek ile iletişime geçebilirsiniz.",
    "Ödeme yöntemleriniz nelerdir?": "Kredi kartı, banka kartı ve kapıda ödeme gibi çeşitli ödeme seçeneklerimiz bulunmaktadır.",
    "İade koşulları nedir?": "Ürünlerimizde iade politikası mevcuttur. 14 gün içinde iade işlemini başlatabilirsiniz.",
}

def get_faq_answer(question):
    # Sorunun cevabını faq_data'dan alıyoruz
    question = question.strip().lower()  # Başındaki ve sonundaki boşlukları temizle ve küçük harfe çevir
    answer = faq_data.get(question, None)

    if answer:
        return answer
    else:
        return "Bu soruya şu anda cevap verilemiyor. Yardımcı olmamı ister misiniz?"