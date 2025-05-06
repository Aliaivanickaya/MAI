from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from app.schemas import EmailCreate, EmailRead, EmailUpdate
from app.services.email_service import EmailService
from app.repositories.email_repository import EmailRepository
from app.auth import verify_token

router = APIRouter(prefix="/emails", tags=["emails"])

email_service = EmailService(EmailRepository())


@router.post("", response_model=EmailRead, dependencies=[Depends(verify_token)])
async def create_email(payload: EmailCreate):
    """
    Создаём новое письмо.
    """
    msg = await email_service.create_email(
        from_user_id=payload.from_user_id,
        to_user_id=payload.to_user_id,
        subject=payload.subject,
        body=payload.body,
        attachments=payload.attachments or []
    )
    return msg.dict()


@router.get("", response_model=List[EmailRead], dependencies=[Depends(verify_token)])
async def list_emails():
    """
    Получить список всех писем.
    """
    msgs = await email_service.list_emails()
    return [m.dict() for m in msgs]


@router.get("/search", response_model=List[EmailRead], dependencies=[Depends(verify_token)])
async def search_emails(subject: str = Query(..., description="Текст темы для поиска")):
    """
    Поиск писем по теме.
    """
    results = await email_service.search_emails_by_subject(subject)
    if not results:
        raise HTTPException(status_code=404, detail="Письма с такой темой не найдены")
    return results


@router.get("/{message_id}", response_model=EmailRead, dependencies=[Depends(verify_token)])
async def get_email(message_id: str):
    """
    Получить конкретное письмо по ID.
    """
    msg = await email_service.get_email(message_id)
    if not msg:
        raise HTTPException(status_code=404, detail="Email not found")
    return msg.dict()


@router.patch("/{message_id}", response_model=EmailRead, dependencies=[Depends(verify_token)])
async def update_email(message_id: str, payload: EmailUpdate):
    """
    Обновление письма (например, пометить как прочитанное).
    """
    if payload.is_read is None:
        raise HTTPException(status_code=400, detail="No fields to update")
    try:
        msg = await email_service.mark_read(message_id, payload.is_read)
        return msg.dict()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{message_id}", dependencies=[Depends(verify_token)])
async def delete_email(message_id: str):
    """
    Удаляем письмо по ID.
    """
    success = await email_service.delete_email(message_id)
    if not success:
        raise HTTPException(status_code=404, detail="Email not found")
    return {"detail": "Email deleted"}
