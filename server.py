from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    movies = [
        {"title": "Inception", "genre": "Sci-Fi"},
        {"title": "Interstellar", "genre": "Sci-Fi"},
        {"title": "The Dark Knight", "genre": "Action"}
    ]
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True)