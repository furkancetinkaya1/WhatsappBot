def home_page():
    return """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>Bot Ana Sayfa</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                color: #333;
                padding: 40px;
            }
            .container {
                max-width: 800px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                text-align: center;
            }
            h1 {
                color: #007bff;
                margin-bottom: 20px;
            }
            p {
                line-height: 1.6;
            }
            .status {
                background-color: #28a745;
                color: white;
                padding: 10px;
                border-radius: 5px;
                margin: 20px 0;
            }
            .button {
                display: inline-block;
                background-color: #007bff;
                color: white;
                padding: 10px 20px;
                margin: 10px;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
                text-align: center;
            }
            .button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>WhatsappBot Ana Sayfa</h1>
            <p>Botumuz şu anda çalışır durumda. Size nasıl yardımcı olabiliriz?</p>
            <div class="status">
                Botumuz aktif ve hazır!
            </div>
            <p>
                <a href="/iletisim" class="button">İletişim</a>
                <a href="/hakkimizda" class="button">Hakkımızda</a>
            </p>
        </div>
    </body>
    </html>
    """