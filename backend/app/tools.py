from langchain_core.tools import tool

from .database import SessionLocal
from .models import Interaction


@tool
def log_interaction(data: dict):
    """
    Save a new interaction into the CRM.
    """

    db = SessionLocal()

    try:

        interaction = Interaction(
            hcp_name=data.get("hcp_name", ""),
            interaction_type=data.get("interaction_type", ""),
            date=data.get("date"),
            time=data.get("time"),
            attendees=data.get("attendees", ""),
            topics=data.get("topics", ""),
            materials=data.get("materials", ""),
            samples=data.get("samples", ""),
            sentiment=data.get("sentiment", ""),
            outcomes=data.get("outcomes", ""),
            followup=data.get("followup", "")
        )

        db.add(interaction)
        db.commit()
        db.refresh(interaction)

        return {
            "status": "success",
            "message": "Interaction logged successfully.",
            "interaction_id": interaction.id
        }

    finally:
        db.close()


@tool
def edit_interaction(interaction_id: int, updated_data: dict):
    """
    Edit an existing interaction.
    """

    db = SessionLocal()

    try:

        interaction = db.query(Interaction).filter(
            Interaction.id == interaction_id
        ).first()

        if not interaction:
            return {
                "status": "error",
                "message": "Interaction not found."
            }

        for key, value in updated_data.items():
            if hasattr(interaction, key):
                setattr(interaction, key, value)

        db.commit()
        db.refresh(interaction)

        return {
            "status": "success",
            "message": "Interaction updated successfully."
        }

    finally:
        db.close()


@tool
def search_hcp(name: str):
    """
    Search HCP by name.
    """

    db = SessionLocal()

    try:

        interactions = db.query(Interaction).filter(
            Interaction.hcp_name.ilike(f"%{name}%")
        ).all()

        results = []

        for item in interactions:
            results.append({
                "id": item.id,
                "hcp_name": item.hcp_name,
                "interaction_type": item.interaction_type,
                "topics": item.topics,
                "followup": item.followup
            })

        return {
            "status": "success",
            "results": results
        }

    finally:
        db.close()


@tool
def interaction_history(hcp_name: str):
    """
    Return all previous interactions.
    """

    db = SessionLocal()

    try:

        interactions = db.query(Interaction).filter(
            Interaction.hcp_name.ilike(f"%{hcp_name}%")
        ).all()

        history = []

        for item in interactions:
            history.append({
                "date": str(item.date),
                "interaction_type": item.interaction_type,
                "topics": item.topics,
                "outcomes": item.outcomes,
                "followup": item.followup
            })

        return {
            "status": "success",
            "history": history
        }

    finally:
        db.close()


@tool
def followup_recommendation(summary: str):
    """
    Generate AI follow-up recommendation.
    """

    recommendation = (
        f"Based on the interaction summary, schedule a follow-up visit "
        f"and share relevant materials. Summary: {summary}"
    )

    return {
        "status": "success",
        "recommendation": recommendation
    }