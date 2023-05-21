from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from messages import queries
from celery import Celery
from sqlalchemy.orm import Session
import smtplib
from config import SMTP_PASSWORD, SMTP_USER, RABBIT_USER, RABBIT_PASS
from messages.database import get_session
from messages.messages import make_template

celery = Celery('tasks', broker=f"amqp://{RABBIT_USER}:{RABBIT_PASS}@80.90.186.118:5672")
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465


@celery.task()
def send_messages(event, session: Session = next(get_session())):
    recipients = queries.read_users(session)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        for recipient in recipients:
            msg = make_template(event, recipient, session)
            server.send_message(msg)
