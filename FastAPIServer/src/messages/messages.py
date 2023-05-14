from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from . import queries
from celery import Celery
from sqlalchemy.orm import Session
import smtplib
from config import SMTP_PASSWORD, SMTP_USER
from .database import get_session

celery = Celery('tasks', broker="redis://localhost:6379")
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465


def make_text_body(event):
    event_data = event.dict()
    return


def make_template(event, session: Session):
    msg = MIMEMultipart()
    msg['Subject'] = 'Новое мероприятие в городе'
    msg['From'] = SMTP_USER
    msg['To'] = queries.read_users(session)
    body = make_text_body(event)
    msg.attach(MIMEText(body, 'plain'))
    return msg


@celery.task()
def send_report(event, session: Session = next(get_session())):
    msg = make_template(session, event)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
