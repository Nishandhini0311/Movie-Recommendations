import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(user_input):
    df = pd.read_csv('data/movies.csv')
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['description'])
    sim_scores = cosine_similarity(tfidf_matrix, tfidf.transform([user_input]))
    top_indices = sim_scores[:,0].argsort()[-5:][::-1]
    return df.iloc[top_indices]
