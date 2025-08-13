import streamlit as st
import pandas as pd
from recommender import recommend_movies, movies

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

st.title("🎬 Movie Recommendation System")
st.write("Find movies similar to your favorites!")

# Movie selection
movie_list = movies['title'].dropna().unique()
selected_movie = st.selectbox("Select a movie:", movie_list)

if st.button("Recommend"):
    recommendations = recommend_movies(selected_movie)
    if len(recommendations) > 0:
        st.write(f"Movies similar to **{selected_movie}**:")
        st.dataframe(recommendations)
    else:
        st.error("Movie not found in dataset.")
