import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.decomposition import PCA  
from sklearn.manifold import TSNE  
from sklearn.cluster import KMeans 
import gensim.downloader as api  

# Load model
model = api.load("word2vec-google-news-300") 

words = ["computer", "AI", "algorithm", "network", "data", "cloud", "software", "hardware", 
         "internet", "machine"] 

# Filter valid words
valid_words = [word for word in words if word in model]
word_vectors = np.array([model[word] for word in valid_words]) 

# PCA
pca = PCA(n_components=10)  
word_vectors_pca = pca.fit_transform(word_vectors) 

# t-SNE
tsne = TSNE(n_components=2, perplexity=5, learning_rate=200, n_iter=3000, random_state=42) 
word_vectors_2D = tsne.fit_transform(word_vectors_pca) 

# KMeans
num_clusters = 3  
kmeans = KMeans(n_clusters=num_clusters, random_state=42)  
clusters = kmeans.fit_predict(word_vectors_2D) 

# Plot
colors = plt.cm.rainbow(np.linspace(0, 1, num_clusters))  
plt.figure(figsize=(10, 8))  

for i, word in enumerate(valid_words):  
    plt.scatter(word_vectors_2D[i, 0], word_vectors_2D[i, 1], color=colors[clusters[i]])  
    plt.annotate(word, (word_vectors_2D[i, 0], word_vectors_2D[i, 1]))  

plt.title("t-SNE Visualization of Technology Word Embeddings with Clusters")  
plt.show()