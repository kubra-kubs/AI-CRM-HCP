from app.graph import graph


print("\n1. Log Interaction Tool")
print(
    graph.invoke({
        "action": "log",
        "data": {
            "hcp_name": "Dr. Ahmed",
            "interaction_type": "Meeting",
            "date": "2026-07-12",
            "time": "10:30",
            "attendees": "Dr. Ahmed",
            "topics": "CardioX",
            "materials": "Clinical brochure",
            "samples": "2",
            "sentiment": "Positive",
            "outcomes": "Doctor showed interest",
            "followup": "Next Friday"
        }
    })
)


print("\n2. Edit Interaction Tool")
print(
    graph.invoke({
        "action": "edit",
        "data": {
            "id": 5,
            "samples": "3",
            "followup": "Next Tuesday"
        }
    })
)


print("\n3. Search HCP Tool")
print(
    graph.invoke({
        "action": "search",
        "data": {
            "hcp_name": "Dr. Sharma"
        }
    })
)


print("\n4. Interaction History Tool")
print(
    graph.invoke({
        "action": "history",
        "data": {
            "hcp_name": "Dr. Sharma"
        }
    })
)


print("\n5. Followup Recommendation Tool")
print(
    graph.invoke({
        "action": "followup",
        "data": {
            "summary": "Doctor showed interest in CardioX"
        }
    })
)