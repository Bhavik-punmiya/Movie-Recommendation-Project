from flask import Flask, request, jsonify
from flask_cors import CORS # Import CORS
from src.components.movie_recommendation_system import MovieRecommendationSystem
from src.components.search_title import SearchTitles
from src.components.similar_movie_recommender import SimilarMovieRecommender

app = Flask(__name__)
CORS(app)
# Initialize the movie recommendation system
recommender_system = MovieRecommendationSystem("artifacts/cleaned_movies.csv", "dataset/ratings.csv", "dataset/movies.csv")

@app.route('/recommend', methods=['GET'])
def recommend_movies():
    # Get the movie title from the query parameters
    title = request.args.get('title', '')
    
    # Recommend movies based on the title
    results = recommender_system.recommend_movies(title)
    
    # Convert the results to JSON format
    results_json = results.to_json(orient='records')
    
    return jsonify(results_json)

@app.route('/recommend_post', methods=['POST'])
def recommend_movies_post():
    # Get the movie title from the JSON body
    data = request.get_json()
    title = data.get('movie', '')
    
    # Recommend movies based on the title
    results = recommender_system.recommend_movies(title)
    
    # Convert the results to JSON format
    results_json = results.to_json(orient='records')
    
    return jsonify(results_json)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
