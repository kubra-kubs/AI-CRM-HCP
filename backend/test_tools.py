from app.graph import graph


print("1. Search HCP")
print(
    graph.invoke({
        "action": "search",
        "data": {
            "hcp_name": "Dr. Sharma"
        }
    })
)


print("\n2. Interaction History")
print(
    graph.invoke({
        "action": "history",
        "data": {
            "hcp_name": "Dr. Sharma"
        }
    })
)


print("\n3. Followup Recommendation")
print(
    graph.invoke({
        "action": "followup",
        "data": {
            "summary": "Doctor showed interest in CardioX"
        }
    })
)