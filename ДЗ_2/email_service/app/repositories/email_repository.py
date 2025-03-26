from typing import List, Optional
from datetime import datetime
from app.models import EmailMessage
from app.db import fake_emails_db, get_next_email_id


class EmailRepository:
    @staticmethod
    def create_email(
        from_user_id: int,
        to_user_id: int,
        subject: str,
        body: str,
        created_at: datetime,
        attachments: list[str]
    ) -> EmailMessage:
        new_id = get_next_email_id()
        msg = EmailMessage(
            message_id=new_id,
            from_user_id=from_user_id,
            to_user_id=to_user_id,
            subject=subject,
            body=body,
            created_at=created_at,
            attachments=attachments
        )
        fake_emails_db[new_id] = msg
        return msg

    @staticmethod
    def get_email_by_id(message_id: int) -> Optional[EmailMessage]:
        return fake_emails_db.get(message_id)

    @staticmethod
    def list_emails() -> List[EmailMessage]:
        return list(fake_emails_db.values())

    @staticmethod
    def update_email(msg: EmailMessage):
        fake_emails_db[msg.message_id] = msg

    @staticmethod
    def delete_email(message_id: int):
        if message_id in fake_emails_db:
            del fake_emails_db[message_id]
