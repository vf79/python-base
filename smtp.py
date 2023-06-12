#!/usr/bin/env python3
"""Exemplos de envio de e-mail

Para testar o envio utilizar servidor de email fake do python rodando o comando:
python -m smtpd -c DebuggingServer -n localhost:8025
As mensagens serão exibidas no terminal.

Para servidores reais buscar tutorial de configuração.
"""

import smtplib

SERVER = "localhost"
PORT = 8025

FROM = "user@user.com"
TO = ["teste02@example.com", "teste02@gmail.com"]
SUBJECT = "Meu e-mail via Python"
TEXT = """\
Este é o meu e-mail enviado pelo Python
<b>Olá terráqueo</b>
"""

# SMTP

message =f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM,TO,message.encode("utf-8"))