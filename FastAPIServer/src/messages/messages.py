from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from celery import Celery
from . import queries
from sqlalchemy.orm import Session
import smtplib
from config import SMTP_PASSWORD, SMTP_USER, RABBIT_USER, RABBIT_PASS
from .database import get_session
celery = Celery('tasks', broker=f"amqp://{RABBIT_USER}:{RABBIT_PASS}@80.90.186.118:5672")
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465


def make_text_body(event):
    return ""


def make_template(event, recipient, session: Session):
    msg = MIMEMultipart()
    msg['Subject'] = 'Новое мероприятие в городе'
    msg['From'] = SMTP_USER
    msg['To'] = recipient
    body = make_text_body(event)
    msg.attach(MIMEText(body, 'plain'))
    return msg


@celery.task()
def send_messages(event, session: Session = next(get_session())):
    recipients = queries.read_users(session)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        for recipient in recipients:
            msg = make_template(event, recipient, session)
            server.send_message(msg)
