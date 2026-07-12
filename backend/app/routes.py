from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

from .schemas import Interaction
from .langgraph_agent import ask_ai
from .database import SessionLocal
from .models import Interaction as InteractionModel

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    data = ask_ai(request.message)

    db = SessionLocal()

    try:

        interaction = InteractionModel(

            hcp_name=data.get("hcp_name", ""),

            interaction_type=data.get("interaction_type", ""),

            date=datetime.today().date(),

            time=datetime.now().time(),

            attendees=data.get("attendees", ""),

            topics=data.get("topics", ""),

            materials=data.get("materials", ""),

            samples=data.get("samples", ""),

            sentiment=data.get("sentiment", ""),

            outcomes=data.get("outcomes", ""),

            followup=data.get("followup", ""),

        )

        db.add(interaction)

        db.commit()

        db.refresh(interaction)

    finally:

        db.close()

    return data