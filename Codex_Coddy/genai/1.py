import numpy as np  
from gensim.downloader import load  
import pprint  

model = load('fasttext-wiki-news-subwords-300')  # 1 GB model 

print("Similar words to 'king': ")  
pprint.pprint(model.most_similar('king')) 

result = model.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)  
print("King - Man + Woman =", result) 

result = model.most_similar(positive=['paris', 'italy'], negative=['france'], topn=1)  
print("Paris - France + Italy =", result) 

vec_king = model['king']  
vec_queen = model['queen']  
vec_man = model['man']  
vec_woman = model['woman'] 

# Fixed line
cosine_similarity = np.dot(vec_king, vec_queen) / (
    np.linalg.norm(vec_king) * np.linalg.norm(vec_queen)
)  

print("Cosine Similarity between 'king' and 'queen':", cosine_similarity) 

result = model.most_similar(positive=['uncle', 'woman'], negative=['man'], topn=1)  
print("Uncle - Man + Woman =", result) 

# Exploring similarities
print("Most similar words to 'good': " + ", ".join(word for word, _ in model.most_similar('good'))) 
print("Most similar words to 'bad': " + ", ".join(word for word, _ in model.most_similar('bad')))