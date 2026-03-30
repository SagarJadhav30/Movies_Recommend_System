import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# Load Data Safely
# -------------------------------
def load_data():
    try:
        with open('movies.pkl', 'rb') as f:
            movies = pickle.load(f)

        # If it's already a DataFrame → use directly
        if isinstance(movies, pd.DataFrame):
            return movies

        # If it's a dict or list → convert
        elif isinstance(movies, (dict, list)):
            return pd.DataFrame(movies)

        else:
            st.error("Unsupported data format in movies.pkl")
            return None

    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None


movies = load_data()

# Stop execution if loading failed
if movies is None:
    st.stop()

def load_similarity():
    try:
        with open('similarity.pkl', 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        st.error(f"Error loading similarity file: {e}")
        return None

similarity = load_similarity()

if similarity is None:
    st.stop()

# -------------------------------
# UI
# -------------------------------
st.title("🎬 Movie Recommender System")

# Check required column exists
if 'title' not in movies.columns:
    st.error("Column 'title' not found in dataset!")
    st.write(movies.head())
    st.stop()

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Select a movie:",
    movie_list
)

# -------------------------------
# Dummy Recommend Function
# -------------------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended = []
    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)

    return recommended


if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies:")
    for i in recommendations:
        st.write(i)