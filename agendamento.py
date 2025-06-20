import smtplib
from email.message import EmailMessage

def enviar_email(destinatario, assunto, corpo):
    email = EmailMessage()
    email['From'] = 'seuemail@gmail.com'
    email['To'] = destinatario
    email['Subject'] = assunto
    email.set_content(corpo)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('fs6136796@gmail.com', 'kcnvgfcviquouhra')  # Senha de app, não sua senha comum
        smtp.send_message(email)

def processar_agendamento():
    usuarios = [
        {"nome": "Alice", "email": "alice@email.com"},
        {"nome": "Bruno", "email": "bruno@email.com"}
    ]

    for usuario in usuarios:
        enviar_email(usuario["email"], "Agendamento Recebido",
                     f"{usuario['nome']}, seu agendamento foi solicitado para 14h.")
        print(f"Agendamento solicitado para {usuario['nome']}")

    for usuario in usuarios:
        enviar_email(usuario["email"], "Agendamento Atendido",
                     f"{usuario['nome']}, seu agendamento foi concluído.")
        print(f"Agendamento atendido para {usuario['nome']}")
