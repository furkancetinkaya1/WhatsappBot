def contact_page():
    return """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>İletişim</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f2f5;
                text-align: center;
                padding: 40px;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 8px;
                max-width: 600px;
                margin: auto;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
            }
            p {
                color: #555;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>İletişim</h1>
            <p>Bizimle iletişime geçmek için <strong>destek@whatsappbot.com</strong> adresine mail atabilirsiniz.</p>
            <p>Ayrıca WhatsApp üzerinden de direkt destek alabilirsiniz.</p>
        </div>
    </body>
    </html>
    """