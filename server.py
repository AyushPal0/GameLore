from fastapi import FastAPI
from dialogue_engine import generate_dialogue

app = FastAPI()

@app.post("/npc")
def npc_response(data: dict):

    player_input = data["player_input"]

    response = generate_dialogue(
        "Dark Mage Arkan",
        "Cold, intelligent, manipulative",
        "Inside forbidden tower",
        player_input
    )

    return {"response": response}
