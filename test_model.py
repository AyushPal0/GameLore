from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "The ancient dragon kingdom was built on"

result = generator(prompt, max_length=60, temperature=0.8)

print(result[0]['generated_text'])
