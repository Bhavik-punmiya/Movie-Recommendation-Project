from .search_title import SearchTitles
from .similar_movie_recommender import SimilarMovieRecommender

class MovieRecommendationSystem:
    def __init__(self, data_path, ratings_path, movies_path):
        self.searcher = SearchTitles(data_path)
        self.recommender = SimilarMovieRecommender(ratings_path, movies_path)

    def recommend_movies(self, title):
        # Perform a cosine similarity search
        search_results = self.searcher.search(title)
        
        # Extract the movieId from the search results
        movie_id = search_results.iloc[0]["movieId"]
        
        # Find similar movies based on user ratings
        similar_movies = self.recommender.find_similar_movies(movie_id)
        
        return similar_movies

if __name__ == "__main__":
    recommender_system = MovieRecommendationSystem("../../artifacts/cleaned_movies.csv", "../../dataset/ratings.csv", "../../dataset/movies.csv")
    search_title = "Toy Story"
    results = recommender_system.recommend_movies(search_title)
    print(results)
