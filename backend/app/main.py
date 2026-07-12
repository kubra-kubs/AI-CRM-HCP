from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import router
from .database import engine
from .models import Base

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to AI CRM HCP Backend 🚀"}

@app.get("/health")
def health():
    return {"status": "Backend is running successfully"}