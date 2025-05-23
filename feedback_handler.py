import json

def save_feedback(movie_title, feedback):
    with open('saved_feedback.json', 'r+') as file:
        data = json.load(file)
        data[movie_title] = feedback
        file.seek(0)
        json.dump(data, file, indent=4)
