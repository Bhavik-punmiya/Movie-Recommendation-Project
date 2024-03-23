import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

class VectorizeAndSave:
    def __init__(self, data_path):
        self.data_path = data_path
        self.tfidf_matrix_path = os.path.join('../../artifacts', "tfidf_matrix.pkl")
        self.vectorizer_path = os.path.join('../../artifacts', "vectorizer.pkl")

    def vectorize_titles(self):
        movies = pd.read_csv(self.data_path)
        # Replace NaN values in the 'clean_title' column with an empty string
        movies['clean_title'] = movies['clean_title'].fillna('')
        vectorizer = TfidfVectorizer(ngram_range=(1,2))
        tfidf = vectorizer.fit_transform(movies["clean_title"])
        return tfidf, vectorizer

    def save_tfidf_matrix(self, tfidf):
        with open(self.tfidf_matrix_path, 'wb') as f:
            pickle.dump(tfidf, f)

    def save_vectorizer(self, vectorizer):
        with open(self.vectorizer_path, 'wb') as f:
            pickle.dump(vectorizer, f)

if __name__ == "__main__":
    vectorizer_saver = VectorizeAndSave("../../artifacts/cleaned_movies.csv")
    tfidf, vectorizer = vectorizer_saver.vectorize_titles()
    vectorizer_saver.save_tfidf_matrix(tfidf)
    vectorizer_saver.save_vectorizer(vectorizer)
