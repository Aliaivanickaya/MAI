from datetime import datetime
from typing import List
from app.models import EmailMessage
from app.repositories.email_repository import EmailRepository


class EmailService:
    def __init__(self, repo: EmailRepository):
        self.repo = repo

    async def create_email(
        self,
        from_user_id: int,
        to_user_id: int,
        subject: str,
        body: str,
        attachments: list[str]
    ) -> EmailMessage:
        return await self.repo.create_email(
            from_user_id=from_user_id,
            to_user_id=to_user_id,
            subject=subject,
            body=body,
            created_at=datetime.utcnow(),
            attachments=attachments
        )

    async def get_email(self, message_id: str) -> EmailMessage | None:
        return await self.repo.get_email_by_id(message_id)

    async def list_emails(self) -> List[EmailMessage]:
        return await self.repo.list_emails()

    async def mark_read(self, message_id: str, is_read: bool) -> EmailMessage:
        msg = await self.repo.get_email_by_id(message_id)
        if not msg:
            raise ValueError("Email not found")
        msg.is_read = is_read
        await self.repo.update_email(msg)
        return msg

    async def search_emails_by_subject(self, subject: str) -> List[EmailMessage]:
        return await self.repo.find_emails_by_subject(subject)

    async def delete_email(self, message_id: str) -> bool:
        msg = await self.repo.get_email_by_id(message_id)
        if not msg:
            return False
        await self.repo.delete_email(message_id)
        return True
