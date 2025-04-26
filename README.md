<p align="center">
  <img src="https://img.shields.io/github/stars/Venki01a/Movie Recommendation System?style=for-the-badge" alt="GitHub Stars Badge"/>
  <img src="https://img.shields.io/github/forks/Venki01a/Movie Recommendation System?style=for-the-badge" alt="GitHub Forks Badge"/>
  <img src="https://img.shields.io/github/issues/Venki01a/Movie Recommendation System?style=for-the-badge" alt="GitHub Issues Badge"/>
  <img src="https://img.shields.io/github/license/Venki01a/Movie Recommendation System?style=for-the-badge" alt="License Badge"/>
</p>


---
# 🎬 Movie Recommendation System

Welcome to the Movie Recommendation System — your personal movie discovery engine!  
This project leverages Natural Language Processing (NLP) and Machine Learning to suggest the most relevant movies based on your preferences. ✨

---

## 📚 Project Highlights

- 🎥 Title-based Recommendations: Start with any movie you love — we’ll find the best similar ones!
- 🎭 Genre, Actor, Director Filters: Fine-tune your search using smart dropdown filters.
- 🌟 Ratings & Release Year Display: Quickly see how good the movie is and when it was released.
- 🔄 Reset Filters: One-click reset to explore new paths easily.
- ⚡ Fast and Lightweight: Powered by TF-IDF vectorization and cosine similarity for blazing fast results.
- 🎨 Modern UI: Smooth, elegant, and intuitive interface built with Streamlit.

---

## 🔥 Features at a Glance

| Feature             | Details                                                                 |
|:--------------------|:------------------------------------------------------------------------|
| Title Search         | Select a movie you like and get recommendations instantly.             |
| Genre Filter         | Choose a specific genre like Action, Drama, or Comedy.                 |
| Actor & Director     | Find movies featuring your favorite actors or directors.               |
| Reset Filters        | Easily reset all selections and start fresh.                           |
| Ratings and Year     | Each movie card shows IMDb-like rating and release year for quick scan.|

---

## 🚀 How it Works

- Data Preprocessing: Merges movie genres, keywords, cast, and director into a unified feature space.
- Vectorization: Uses TF-IDF to convert movie features into numerical vectors.
- Similarity Computation: Calculates similarity between movies using cosine similarity.
- Recommendation Logic: Filters the recommendations based on user input dynamically.

---

## 🛠️ Built With

- Python 🐍
- Streamlit 🚀 (for front-end deployment)
- Pandas (for data handling)
- Scikit-learn (for TF-IDF vectorization and similarity calculation)

---

> 🔥 *"Discover your next favorite movie in just a few clicks!"*

---

## 📂 Folder Structure

```
/movie-recommendation-system
│
├── Movies.csv              # Dataset
├── app.py                  # Streamlit application code
├── requirements.txt        # List of dependencies
└── README.md                # Project overview (this file)
```

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/your-username/movie-recommendation-system.git

# Navigate into the directory
cd movie-recommendation-system

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

✅ That's it — you're ready to explore endless movie recommendations!

---

## ✨ Future Enhancements

- Add poster images next to recommendations 📷
- Incorporate real-time data from IMDb or TMDb APIs 🌐
- Improve filtering with multi-select options 🎯
- Deploy online using Streamlit Cloud, AWS, or Render ☁️

---

> ⭐ If you like the project, feel free to give it a star and share it with your movie-lover friends!

---

# 🎥 *"Because great movies deserve great recommendations."* 🎬

---

---
