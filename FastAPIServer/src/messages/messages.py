from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from sqlalchemy.orm import Session

from config import SMTP_USER


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
