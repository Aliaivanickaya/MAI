import uvicorn
from fastapi import FastAPI

from app.routers import folder_router

app = FastAPI(title="Folder Service")
app.include_router(folder_router.router)


if __name__ == "__main__":
    uvicorn.run("main:main_app", host="0.0.0.0", port=8000, reload=True)
