import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("Movies.csv")

# Fill missing values
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
for feature in selected_features:
    data[feature] = data[feature].fillna('')

# Combine selected features
combined_features = data[selected_features].apply(lambda row: ' '.join(row.values), axis=1)

# Vectorization
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Cosine Similarity
similarity = cosine_similarity(feature_vectors)

# Streamlit page setup
st.set_page_config(page_title="🎬 Movie Recommender (with Reset & Ratings)", layout="centered")
st.title("🎥 Movie Recommendation System")
st.write("Select your preferences to discover amazing movies!")

# Sidebar for filters
st.sidebar.header("🔎 Filters")

# Dropdowns
movie_titles = sorted(data['title'].dropna().unique())
all_genres = sorted(set(g.strip() for sublist in data['genres'].dropna().str.split('|') for g in sublist))
all_actors = sorted(set(actor.strip() for sublist in data['cast'].dropna().str.split('|') for actor in sublist))
all_directors = sorted(data['director'].dropna().unique())

# Default values
default_movie = movie_titles[0]
default_genre = 'Any'
default_actor = 'Any'
default_director = 'Any'

# Session state for reset functionality
if 'reset' not in st.session_state:
    st.session_state.reset = False

if st.session_state.reset:
    selected_movie = st.sidebar.selectbox("Select a Movie Title", options=movie_titles, index=0)
    selected_genre = st.sidebar.selectbox("Select a Genre (optional)", options=['Any'] + all_genres, index=0)
    selected_actor = st.sidebar.selectbox("Select an Actor (optional)", options=['Any'] + all_actors, index=0)
    selected_director = st.sidebar.selectbox("Select a Director (optional)", options=['Any'] + list(all_directors), index=0)
    st.session_state.reset = False
else:
    selected_movie = st.sidebar.selectbox("Select a Movie Title", options=movie_titles)
    selected_genre = st.sidebar.selectbox("Select a Genre (optional)", options=['Any'] + all_genres)
    selected_actor = st.sidebar.selectbox("Select an Actor (optional)", options=['Any'] + all_actors)
    selected_director = st.sidebar.selectbox("Select a Director (optional)", options=['Any'] + list(all_directors))

# Reset button
if st.sidebar.button("Reset Filters"):
    st.session_state.reset = True
    st.rerun()

# Main Button
if st.button("Recommend"):
    movie_list_lower = data['title'].str.lower().tolist()
    selected_movie_lower = selected_movie.lower().strip()

    if selected_movie_lower in movie_list_lower:
        index_of_movie = movie_list_lower.index(selected_movie_lower)
        similarity_score = list(enumerate(similarity[index_of_movie]))
        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

        st.subheader("🎯 Top Recommended Movies for You:")
        count = 0

        for movie in sorted_similar_movies:
            index = movie[0]
            movie_data = data.iloc[index]

            title = movie_data['title']
            genres = movie_data['genres']
            cast = movie_data['cast']
            director = movie_data['director']
            rating = movie_data.get('vote_average', 'N/A')  # Adjust this if your rating column is named differently
            release_date = movie_data.get('release_date', 'N/A')
            if pd.notna(release_date):
                release_year = str(release_date).split('-')[0]
            else:
                release_year = "Unknown"

            # Apply Filters
            if title.lower() != selected_movie_lower:
                if selected_genre != 'Any' and selected_genre.lower() not in genres.lower():
                    continue
                if selected_actor != 'Any' and selected_actor.lower() not in cast.lower():
                    continue
                if selected_director != 'Any' and selected_director.lower() not in director.lower():
                    continue

                st.write(f"**{count+1}. {title} ({release_year})** - ⭐ {rating}")
                count += 1

            if count == 10:
                break
    else:
        st.error("Selected movie not found!")
