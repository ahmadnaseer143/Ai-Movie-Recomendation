import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {'title': ['Inception', 'The Matrix', 'Interstellar', 'The Dark Knight', 'Avatar'], 'overview': ['A thief who steals corporate secrets through dream-sharing technology.', 'A computer hacker learns about the true nature of reality and his role in the war.', "A team of explorers travel through a wormhole in space to ensure humanity's survival.", 'When the menace known as the Joker wreaks havoc in Gotham, Batman must accept his greatest test.', 'A marine on an alien planet becomes torn between following orders and protecting his home.'], 'genres': ['Action Sci-Fi Thriller', 'Action Sci-Fi', 'Adventure Drama Sci-Fi', 'Action Crime Drama', 'Action Adventure Fantasy']}

df = pd.DataFrame(data)
df['combined'] = df['overview'] + ' ' + df['genres']
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

def get_recommendations(title, num_recommendations=5):
    if title not in indices:
        return []
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations + 1]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()
