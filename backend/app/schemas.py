from pydantic import BaseModel


class Interaction(BaseModel):
    hcp_name: str
    interaction_type: str
    date: str
    time: str
    attendees: str
    topics: str
    materials: str
    samples: str
    sentiment: str
    outcomes: str
    followup: str