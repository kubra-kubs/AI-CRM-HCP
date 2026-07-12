from sqlalchemy import Column, Integer, String, Text, Date, Time
from app.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_name = Column(String(100))
    interaction_type = Column(String(50))

    date = Column(Date)
    time = Column(Time)

    attendees = Column(Text)
    topics = Column(Text)

    materials = Column(Text)
    samples = Column(Text)

    sentiment = Column(String(20))

    outcomes = Column(Text)
    followup = Column(Text)