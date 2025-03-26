from datetime import datetime
from typing import List
from app.models import EmailMessage
from app.repositories.email_repository import EmailRepository


class EmailService:
    def __init__(self, repo: EmailRepository):
        self.repo = repo

    def create_email(
        self,
        from_user_id: int,
        to_user_id: int,
        subject: str,
        body: str,
        attachments: list[str]
    ) -> EmailMessage:
        return self.repo.create_email(
            from_user_id=from_user_id,
            to_user_id=to_user_id,
            subject=subject,
            body=body,
            created_at=datetime.utcnow(),
            attachments=attachments
        )

    def get_email(self, message_id: int) -> EmailMessage | None:
        return self.repo.get_email_by_id(message_id)

    def list_emails(self) -> List[EmailMessage]:
        return self.repo.list_emails()

    def mark_read(self, message_id: int, is_read: bool) -> EmailMessage:
        msg = self.repo.get_email_by_id(message_id)
        if not msg:
            raise ValueError("Email not found")
        msg.is_read = is_read
        self.repo.update_email(msg)
        return msg

    def delete_email(self, message_id: int) -> bool:
        msg = self.repo.get_email_by_id(message_id)
        if not msg:
            return False
        self.repo.delete_email(message_id)
        return True
