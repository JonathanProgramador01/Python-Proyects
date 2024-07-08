# class NotificationManager:
#     #This class is responsible for sending notifications with the deal flight details.
#     pass

import os
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


def send_whatsapp(text: str):
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=text,
        to='whatsapp:+5215580327685'
    )

    print(message.sid)


def send_mensaje(text: str):
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=text,
        from_="+14325580336",
        to="+525580327685",
    )

    print(message.body)


def send_gmails(gmails: list,mensaje: str):
    for gmail in gmails:
        FROM = os.environ.get("GMAIL")
        TO = gmail
        HOST = "smtp.gmail.com"
        PASWORD = os.environ.get("CONTRASEÑA")
        coneccion = smtplib.SMTP(HOST)
        coneccion.starttls()
        coneccion.login(user=FROM,password=PASWORD)
        coneccion.sendmail(from_addr=FROM,to_addrs=TO,msg=f"Subject:OFERTAA DE VUELOSSS\n\n{mensaje}")
        coneccion.close()
        print("SEM MANDOO GMAIL CON EXITOOO")


