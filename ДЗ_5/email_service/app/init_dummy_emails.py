import asyncio
import os
import random

from faker import Faker
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.getenv("MONGODB_URL", "mongodb://mongo_db:27017")
DB_NAME   = os.getenv("MONGODB_DB", "email_db")

NUM_EMAILS = 50

MIN_EXISTING = 10

fake = Faker()

async def init_dummy_emails():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]
    col = db.emails

    count = await col.count_documents({})
    if count > MIN_EXISTING:
        print(f"Найдено {count} писем — инициализация не потребуется.")
        client.close()
        return

    print(f"Генерация {NUM_EMAILS} тестовых писем...")
    docs = []
    for _ in range(NUM_EMAILS):
        from_user_id = fake.random_int(min=1, max=50)
        to_user_id   = fake.random_int(min=1, max=50)
        subject      = fake.sentence(nb_words=6)
        body         = "\n\n".join(fake.paragraphs(nb=random.randint(1, 4)))
        created_at   = fake.date_time_between(start_date="-30d", end_date="now")
        is_read      = fake.boolean(chance_of_getting_true=50)
        attachments  = [
            fake.file_name(extension=random.choice(["pdf", "jpg", "png", "docx"]))
            for _ in range(random.randint(0, 3))
        ]

        docs.append({
            "from_user_id": from_user_id,
            "to_user_id": to_user_id,
            "subject": subject,
            "body": body,
            "created_at": created_at,
            "is_read": is_read,
            "attachments": attachments,
        })

    result = await col.insert_many(docs)
    print(f"Вставлено писем: {len(result.inserted_ids)}")
    client.close()

if __name__ == "__main__":
    asyncio.run(init_dummy_emails())
