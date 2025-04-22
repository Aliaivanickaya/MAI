from typing import List, Optional
from datetime import datetime
from bson import ObjectId

from app.models import EmailMessage
from app.db import db


class EmailRepository:
    collection = db.emails

    @staticmethod
    async def create_email(
        from_user_id: int,
        to_user_id: int,
        subject: str,
        body: str,
        created_at: datetime,
        attachments: List[str],
        is_read: bool = False
    ) -> EmailMessage:
        doc = {
            "from_user_id": from_user_id,
            "to_user_id": to_user_id,
            "subject": subject,
            "body": body,
            "created_at": created_at,
            "is_read": is_read,
            "attachments": attachments
        }
        result = await EmailRepository.collection.insert_one(doc)
        return EmailMessage(
            message_id=str(result.inserted_id),
            from_user_id=from_user_id,
            to_user_id=to_user_id,
            subject=subject,
            body=body,
            created_at=created_at,
            is_read=is_read,
            attachments=attachments
        )

    @staticmethod
    async def get_email_by_id(message_id: str) -> Optional[EmailMessage]:
        doc = await EmailRepository.collection.find_one({"_id": ObjectId(message_id)})
        if not doc:
            return None
        return EmailMessage(
            message_id=str(doc["_id"]),
            from_user_id=doc["from_user_id"],
            to_user_id=doc["to_user_id"],
            subject=doc["subject"],
            body=doc["body"],
            created_at=doc["created_at"],
            is_read=doc.get("is_read", False),
            attachments=doc.get("attachments", [])
        )

    @staticmethod
    async def list_emails() -> List[EmailMessage]:
        emails: List[EmailMessage] = []
        async for doc in EmailRepository.collection.find():
            emails.append(
                EmailMessage(
                    message_id=str(doc["_id"]),
                    from_user_id=doc["from_user_id"],
                    to_user_id=doc["to_user_id"],
                    subject=doc["subject"],
                    body=doc["body"],
                    created_at=doc["created_at"],
                    is_read=doc.get("is_read", False),
                    attachments=doc.get("attachments", [])
                )
            )
        return emails

    @staticmethod
    async def update_email(msg: EmailMessage) -> None:
        await EmailRepository.collection.update_one(
            {"_id": ObjectId(msg.message_id)},
            {"$set": {
                "from_user_id": msg.from_user_id,
                "to_user_id": msg.to_user_id,
                "subject": msg.subject,
                "body": msg.body,
                "created_at": msg.created_at,
                "is_read": msg.is_read,
                "attachments": msg.attachments
            }}
        )

    @staticmethod
    async def find_emails_by_subject(subject: str) -> List[EmailMessage]:
        query: dict = {"subject": subject}
        emails: List[EmailMessage] = []
        async for doc in EmailRepository.collection.find(query):
            emails.append(
                EmailMessage(
                    message_id=str(doc["_id"]),
                    from_user_id=doc["from_user_id"],
                    to_user_id=doc["to_user_id"],
                    subject=doc["subject"],
                    body=doc["body"],
                    created_at=doc["created_at"],
                    is_read=doc.get("is_read", False),
                    attachments=doc.get("attachments", [])
                )
            )
        return emails

    @staticmethod
    async def delete_email(message_id: str) -> None:
        await EmailRepository.collection.delete_one({"_id": ObjectId(message_id)})
