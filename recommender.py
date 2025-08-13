import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load movies dataset
movies = pd.read_csv("Movies dataset/movies_metadata.csv", low_memory=False)

# Reset index
movies = movies.reset_index(drop=True)

# Fill missing overviews
movies['overview'] = movies['overview'].fillna('')

# Create TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])

# Compute cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Build mapping of movie titles to indices
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

def recommend_movies(title, num_recommendations=10):
    if title not in indices:
        return []
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies[['title', 'vote_average', 'vote_count']].iloc[movie_indices]
