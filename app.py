import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load dataset
df = pd.read_csv('movies.csv')

# TF-IDF on genres
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genres'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Recommendation function
def recommend_movie(title):
    if title not in df['title'].values:
        return ["Movie not found. Try a different name."]
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()

# Streamlit UI
st.title("AI Movie Recommender")
movie = st.selectbox("Select a movie you liked:", df['title'].values)
if st.button("Recommend"):
    st.write("You may also like:")
    for m in recommend_movie(movie):
        st.write(f"- {m}")
