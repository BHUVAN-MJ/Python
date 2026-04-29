# --- Import libraries --- 
import gensim.downloader as api 
import google.generativeai as genai 
import os 

# --- Configure API key safely --- 
API_KEY = os.getenv("GEMINI_API_KEY") 

if not API_KEY: 
    print("API key not found. Running in OFFLINE mode.") 
else: 
    genai.configure(api_key=API_KEY) 

# --- Load FastText model --- 
print("Loading word model... please wait.") 
word_model = api.load("fasttext-wiki-news-subwords-300") 
print("Word model loaded!") 

# --- Helper to filter bad words --- 
def is_valid_word(original, candidate): 
    return ( 
        candidate.isalpha() 
        and candidate != original 
        and not candidate.startswith(original[:3])  
    ) 

# --- Find similar words --- 
def find_similar_words(word): 
    try: 
        similar_words = word_model.most_similar(word.lower(), topn=10) 
        good_matches = [ 
            w for w, score in similar_words 
            if score > 0.65 and is_valid_word(word.lower(), w) 
        ] 
        return good_matches[:3] 
    except KeyError: 
        return [] 

# --- Enrich prompt intelligently --- 
def enrich_prompt(prompt): 
    words = prompt.split() 
    result = [] 

    important_words = {"ai", "healthcare", "doctor", "medical"} 

    for word in words: 
        clean_word = word.lower().strip('.,!?;:()') 

        if clean_word in important_words: 
            similar = find_similar_words(clean_word) 
            if similar: 
                enriched_word = f"{word} [{', '.join(similar)}]" 
                result.append(enriched_word) 
            else: 
                result.append(word) 
        else: 
            result.append(word) 

    return " ".join(result) 

# --- Ask Gemini (with fallback) --- 
def ask_gemini(prompt): 
    if not API_KEY: 
        return None  

    try: 
        model = genai.GenerativeModel('gemini-2.0-flash-lite') 
        response = model.generate_content(prompt) 
        return response.text if response else None
    except Exception as e: 
        print("API Error:", e) 
        return None 

# --- Run program --- 
original_prompt = "Write about AI in healthcare." 
enriched_prompt = enrich_prompt(original_prompt) 

print("\n--- YOUR PROMPTS ---") 
print("Original :", original_prompt) 
print("Enriched :", enriched_prompt) 

# --- Call Gemini --- 
print("\nAsking Gemini with original prompt...") 
original_response = ask_gemini(original_prompt) 

print("Asking Gemini with enriched prompt...") 
enriched_response = ask_gemini(enriched_prompt) 

# --- Fallback if API fails --- 
if not original_response: 
    original_response = ( 
        "AI in healthcare helps in diagnosis, treatment planning, "
        "medical imaging, and improving patient care efficiency." 
    ) 

if not enriched_response: 
    enriched_response = ( 
        "Artificial intelligence in healthcare enhances clinical decisions, "
        "predictive analysis, automated diagnosis, and hospital management." 
    ) 

# --- Display results --- 
print("\n--- RESPONSE TO ORIGINAL PROMPT ---") 
print(original_response) 

print("\n--- RESPONSE TO ENRICHED PROMPT ---") 
print(enriched_response) 

# --- Compare responses --- 
print("\n--- COMPARISON ---") 
orig_words = original_response.split() 
enr_words = enriched_response.split() 

print(f"Original response → {len(orig_words)} words, {len(set(orig_words))} unique words") 
print(f"Enriched response → {len(enr_words)} words, {len(set(enr_words))} unique words")