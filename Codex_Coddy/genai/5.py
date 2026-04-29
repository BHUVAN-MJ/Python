# ----------- Import Libraries ----------- 
import gensim.downloader as api 
import google.generativeai as genai 
import os 
import random 
import numpy as np 

# ----------- Configure API Key (OPTIONAL) ----------- 
API_KEY = os.getenv("GEMINI_API_KEY") 

if API_KEY: 
    genai.configure(api_key=API_KEY) 
    print("Gemini API configured") 
else: 
    print("Running in OFFLINE mode (Template-based generation)") 

# ----------- Load Small Embedding Model ----------- 
try: 
    print("Loading model...") 
    model = api.load("glove-wiki-gigaword-50")  # small & fast 
    print("Model loaded successfully") 
except: 
    print("Model loading failed. Using fallback mode.") 
    model = None 

# ----------- Cosine Similarity Function ----------- 
def cosine_similarity(vec1, vec2): 
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)) 

# ----------- Get Similar Words ----------- 
def get_similar_words(word, top_n=5): 
    if not model: 
        return [] 
    try: 
        word_vec = model[word] 
        all_words = list(model.index_to_key) 
        similarities = [] 

        for w in all_words: 
            if w.isalpha() and w != word: 
                sim = cosine_similarity(word_vec, model[w]) 
                similarities.append((w, sim)) 

        similarities.sort(key=lambda x: x[1], reverse=True) 
        return [w for w, _ in similarities[:top_n]] 
    except: 
        return [] 

# ----------- Offline Paragraph Generation ----------- 
def generate_paragraph(seed_word): 
    similar_words = get_similar_words(seed_word) 

    if len(similar_words) < 5: 
        return f"Could not generate content for '{seed_word}'" 

    templates = [ 
        f"The {seed_word} traveled across {similar_words[0]} lands, facing {similar_words[1]} challenges. "
        f"It discovered {similar_words[2]} secrets and {similar_words[3]} adventures, guided by {similar_words[4]}.",

        f"In the world of {seed_word}, people explored {similar_words[0]} ideas and {similar_words[1]} innovations. "
        f"With {similar_words[2]} tools and {similar_words[3]} thinking, they achieved {similar_words[4]} success."
    ] 

    return random.choice(templates) 

# ----------- Gemini Function ----------- 
def ask_gemini(prompt): 
    if not API_KEY: 
        return None 

    try: 
        model_gen = genai.GenerativeModel('gemini-2.0-flash-lite') 
        response = model_gen.generate_content(prompt) 
        return response.text if response else None 
    except Exception as e: 
        print("API Error:", e) 
        return None 

# ----------- Main Program ----------- 
seed_word = input("Enter a seed word: ") 

# Try Generative AI 
ai_output = ask_gemini(f"Write a creative paragraph about {seed_word}") 

# Output Selection 
if ai_output: 
    print("\n--- Gemini Generated Output ---") 
    print(ai_output) 
else: 
    print("\n--- Offline Generated Output ---") 
    print(generate_paragraph(seed_word))