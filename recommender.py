import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1) Load CSV
df = pd.read_csv("tmdb_movies.csv")

# 2) Clean NaN values
df['overview'] = df['overview'].fillna('')
df['genres'] = df['genres'].fillna('')

# 3) Create combined column
df['combined'] = df['overview'] + ' ' + df['genres']

# 4) TF-IDF & Cosine Similarity
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

# 5) Recommendation function
from difflib import get_close_matches

def get_recommendations(title, num_recommendations=5):
    if title not in indices:
        # Try fuzzy matching
        possible_titles = get_close_matches(title, df['title'].tolist(), n=3, cutoff=0.6)
        if possible_titles:
            title = possible_titles[0]  # take closest match
        else:
            return []  # no similar title found

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations + 1]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()


def get_movies():
    return df['title'].tolist()