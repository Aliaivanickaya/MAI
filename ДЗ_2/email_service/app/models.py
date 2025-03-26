from datetime import datetime
from typing import List, Optional


class EmailMessage:
    """
    Доменная модель письма.
    from_user_id, to_user_id -- идентификаторы пользователей (int),
    subject, body -- текст письма,
    created_at -- время создания,
    is_read -- флаг, прочитано ли письмо.
    attachments -- список строк.
    """
    def __init__(
        self,
        message_id: int,
        from_user_id: int,
        to_user_id: int,
        subject: str,
        body: str,
        created_at: datetime,
        is_read: bool = False,
        attachments: Optional[List[str]] = None,
    ):
        self.message_id = message_id
        self.from_user_id = from_user_id
        self.to_user_id = to_user_id
        self.subject = subject
        self.body = body
        self.created_at = created_at
        self.is_read = is_read
        self.attachments = attachments or []

    def dict(self) -> dict:
        return {
            "message_id": self.message_id,
            "from_user_id": self.from_user_id,
            "to_user_id": self.to_user_id,
            "subject": self.subject,
            "body": self.body,
            "created_at": self.created_at.isoformat(),
            "is_read": self.is_read,
            "attachments": self.attachments
        }
