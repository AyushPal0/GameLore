from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 1️⃣ Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2️⃣ Load lore file
with open("lore.txt", "r") as f:
    lore_data = f.readlines()

# 3️⃣ Convert lore into embeddings
lore_embeddings = model.encode(lore_data)

# 4️⃣ Create FAISS index
dimension = lore_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(lore_embeddings))

# 5️⃣ ADD THIS FUNCTION HERE 👇
def retrieve_lore(query):

    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k=1)

    return lore_data[indices[0][0]]
