# Not: Bu sözlükteki anahtarlar doğrudan kullanılmaz. Kullanıcının mesajı .strip().lower() ile normalize edilmelidir.
faq_data = {
    "1": "Botun çalışma durumu nedir?",
    "2": "Hangi ürünleri satıyorsunuz?",
    "3": "Ürünlerin fiyatları nasıl?",
    "4": "Nasıl sipariş verebilirim?",
    "5": "Ödeme yöntemleriniz nelerdir?",
    "6": "İade koşulları nedir?",
}

faq_answers = {
    "1": "Botumuz şu anda aktif ve size yardımcı olmaya hazır!",
    "2": "Çeşitli elektronik ürünler, telefonlar, bilgisayarlar ve aksesuarlar satıyoruz.",
    "3": "Ürünlerin fiyatları, model ve özelliklerine göre değişmektedir. Detaylı fiyat bilgisi için ürün sayfasını ziyaret edebilirsiniz.",
    "4": "Ürünleri sepete ekleyebilir ve ödeme işlemini gerçekleştirebilirsiniz. Yardıma ihtiyacınız varsa canlı destek ile iletişime geçebilirsiniz.",
    "5": "Kredi kartı, banka kartı ve kapıda ödeme gibi çeşitli ödeme seçeneklerimiz bulunmaktadır.",
    "6": "Ürünlerimizde iade politikası mevcuttur. 14 gün içinde iade işlemini başlatabilirsiniz.",
}

def get_faq_answer(question_number):
    # Sorunun numarasını alıp cevapları getiriyoruz
    answer = faq_answers.get(question_number, "Bu soruya şu anda cevap verilemiyor. Yardımcı olmamı ister misiniz?")

    return answer