def homePage():
    return """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WhatsApp E-Ticaret Botu</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                padding: 40px;
            }
            h1 {
                color: #2c3e50;
            }
            p {
                color: #34495e;
                font-size: 1.2em;
            }
            .container {
                max-width: 600px;
                margin: auto;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>👋 WhatsApp E-Ticaret Botuna Hoş Geldiniz!</h1>
            <p>Bu bot sayesinde ürün bilgilerini alabilir, sipariş sürecinizi başlatabilirsiniz.</p>
            <p>WhatsApp üzerinden mesaj göndererek hemen iletişime geçebilirsiniz.</p>
        </div>
    </body>
    </html>
    """