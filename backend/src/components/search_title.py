import os
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

class SearchTitles:
    def __init__(self, data_path):
        self.data_path = data_path
        self.tfidf_matrix_path = os.path.join('artifacts', "tfidf_matrix.pkl")
        self.vectorizer_path = os.path.join('artifacts', "vectorizer.pkl")

    def load_tfidf_matrix(self):
        with open(self.tfidf_matrix_path, 'rb') as f:
            tfidf = pickle.load(f)
        return tfidf

    def load_vectorizer(self):
        with open(self.vectorizer_path, 'rb') as f:
            vectorizer = pickle.load(f)
        return vectorizer

    def search(self, title):
        movies = pd.read_csv(self.data_path)
        vectorizer = self.load_vectorizer()
        query_vec = vectorizer.transform([title])
        tfidf = self.load_tfidf_matrix()
        similarity = cosine_similarity(query_vec, tfidf).flatten()
        indices = np.argpartition(similarity, -5)[-5:]
        results = movies.iloc[indices].iloc[::-1]
        return results

if __name__ == "__main__":
    searcher = SearchTitles("../../artifacts/cleaned_movies.csv")
    search_title = "End game"
    results = searcher.search(search_title)
    print(results)
