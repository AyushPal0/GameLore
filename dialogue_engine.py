from transformers import pipeline
from lore_system import retrieve_lore


generator = pipeline("text-generation", model="gpt2")

conversation_memory = []

def generate_dialogue(character_name, personality, situation, player_input):
    
    global conversation_memory
    
    conversation_memory.append(f"Player: {player_input}")
    
    memory_text = "\n".join(conversation_memory[-5:])  # last 5 messages
    
    relevant_lore = retrieve_lore(player_input)

    prompt = f"""
    You are {character_name}.
    Personality: {personality}
    Current Situation: {situation}
    Player says: {player_input}
    
    World Lore:
    {relevant_lore}
    
    Previous conversation:
    {memory_text}
    
    Player says: {player_input}

    Respond in character:
    """

    result = generator(prompt, max_length=150, temperature=0.9)

    reply = result[0]['generated_text']
    
    conversation_memory.append(f"{character_name}: {reply}")
    
    return reply

# Example
print(generate_dialogue(
    "Dark Mage Arkan",
    "Cold, intelligent, manipulative",
    "Player has entered forbidden tower",
    "Why are you attacking the kingdom?"
))
