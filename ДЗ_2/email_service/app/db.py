from typing import Dict
from app.models import EmailMessage

fake_emails_db: Dict[int, EmailMessage] = {}
fake_email_id_seq = 0


def get_next_email_id() -> int:
    global fake_email_id_seq
    fake_email_id_seq += 1
    return fake_email_id_seq
