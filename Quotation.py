import requests
import smtplib
import email.message
from datetime import datetime


# Get the information through the Awesome API
request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL")
request_dict = request.json()
quot_dollar = float(request_dict['USDBRL']['bid'])
quot_euro = float(request_dict['EURBRL']['bid'])
print(f"A cotação do euro é: {quot_euro}")
print(f"A cotação do dollar é: {quot_dollar}")


# Send mail containing the information/quotation
def send_email(quot_dollar, quot_euro):
    email_body = f"""
    <h1>Cotação atual</h1>
    <p><h2>Olá,</h2> fique ligado nas cotações atuais das principais moedas:</p>
    <p>Dólar: <strong>R${quot_dollar}</strong><br>
    Euro: <strong>R${quot_euro}</strong></p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Cotação atual, dólar e euro."
    msg['From'] = 'from'
    msg['To'] = 'to'
    password = 'password'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print(f"Email sent. {datetime.now()}")

send_email(quot_dollar, quot_euro)

