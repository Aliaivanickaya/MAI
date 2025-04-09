import uvicorn
from fastapi import FastAPI

from app.routers import email_router

app = FastAPI(title="Email Service")
app.include_router(email_router.router)


if __name__ == "__main__":
    uvicorn.run("main:main_app", host="0.0.0.0", port=8000, reload=True)
