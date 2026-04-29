# !pip install wikipedia-api

import wikipediaapi 
from gensim.models import Word2Vec 
from gensim.utils import simple_preprocess 
import random 

# Initialize Wikipedia API 
wiki_wiki = wikipediaapi.Wikipedia(
    user_agent='my-medical-bot (your_email@example.com)', 
    language='en'
) 

# List of medical topics 
medical_topics = ["Diabetes", "Alzheimer's disease", "Hypertension", "Cardiology", "Oncology"] 

# Extract corpus 
medical_corpus = [] 

for topic in medical_topics: 
    page = wiki_wiki.page(topic) 
    if page.exists(): 
        sentences = page.text.split(". ") 
        medical_corpus.extend(sentences) 

# Sample sentences 
medical_corpus = random.sample(medical_corpus, min(500, len(medical_corpus))) 

# Tokenize 
tokenized_corpus = [
    simple_preprocess(sentence) 
    for sentence in medical_corpus 
    if sentence.strip() != ""
] 

# Train Word2Vec 
model = Word2Vec( 
    sentences=tokenized_corpus, 
    vector_size=100, 
    window=5, 
    min_count=2, 
    workers=4, 
    sg=1 
) 

# Save & Load 
model.save("medical_word2vec_wiki.model") 
loaded_model = Word2Vec.load("medical_word2vec_wiki.model") 

# Test 
if 'diabetes' in loaded_model.wv: 
    print("Words similar to 'diabetes':") 
    for word, similarity in loaded_model.wv.most_similar("diabetes"): 
        print(f"{word} : {similarity:.4f}") 
else: 
    print("'diabetes' not found in the vocabulary.")