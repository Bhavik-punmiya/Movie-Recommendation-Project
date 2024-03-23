import pandas as pd

class SimilarMovieRecommender:
    def __init__(self, ratings_path, movies_path):
        self.ratings = pd.read_csv(ratings_path)
        self.movies = pd.read_csv(movies_path)

    def find_similar_movies(self, movie_id):
        similar_users = self.ratings[(self.ratings["movieId"] == movie_id) & (self.ratings["rating"] > 4)]["userId"].unique()
        similar_user_recs = self.ratings[(self.ratings["userId"].isin(similar_users)) & (self.ratings["rating"] > 4)]["movieId"]
        similar_user_recs = similar_user_recs.value_counts() / len(similar_users)

        similar_user_recs = similar_user_recs[similar_user_recs > .10]
        all_users = self.ratings[(self.ratings["movieId"].isin(similar_user_recs.index)) & (self.ratings["rating"] > 4)]
        all_user_recs = all_users["movieId"].value_counts() / len(all_users["userId"].unique())
        rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
        rec_percentages.columns = ["similar", "all"]
        
        rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
        rec_percentages = rec_percentages.sort_values("score", ascending=False)

        return rec_percentages.head(12).merge(self.movies, left_index=True, right_on="movieId")[["score", "title", "genres"]]

if __name__ == "__main__":
    recommender = SimilarMovieRecommender("../../dataset/ratings.csv", "../../artifacts/cleaned_movies.csv")
    movie_id = 1 # Example movie ID
    results = recommender.find_similar_movies(movie_id)
    print(results)
