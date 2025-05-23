from flask import Flask, render_template, request
from recommender import get_recommendations

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['user_input']
        recommendations = get_recommendations(user_input)
        return render_template('index.html', movies=recommendations)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
