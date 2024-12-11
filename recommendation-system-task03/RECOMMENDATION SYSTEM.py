import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Collaborative Filtering Example

# Step 1: Create User-Item Interaction Matrix
data = {
    'User': [1, 2, 3, 4],
    'Movie A': [5, 4, 0, 2],
    'Movie B': [3, 0, 5, 0],
    'Movie C': [0, 0, 4, 0],
    'Movie D': [1, 1, 0, 5]
}
df = pd.DataFrame(data).set_index('User')

# Step 2: Calculate Similarity
similarity = cosine_similarity(df.fillna(0))
similarity_df = pd.DataFrame(similarity, index=df.index, columns=df.index)

# Step 3: Make Recommendations
def get_recommendations(user_id):
    similar_users = similarity_df[user_id].sort_values(ascending=False)
    similar_users = similar_users.loc[similar_users.index != user_id]
    
    recommendations = pd.Series(dtype='float')
    
    for other_user in similar_users.index:
        recommendations = recommendations.add(df.loc[other_user], fill_value=0)

    recommendations = recommendations.sort_values(ascending=False)
    return recommendations[recommendations > 0].index.tolist()

# Example usage of Collaborative Filtering
print("Collaborative Filtering Recommendations for User 1:")
print(get_recommendations(1))

# Content-Based Filtering Example

# Step 1: Create Item Features
items = pd.DataFrame({
    'Movie': ['Movie A', 'Movie B', 'Movie C', 'Movie D'],
    'Genre': ['Action', 'Drama', 'Comedy', 'Action'],
    'Description': [
        'An action packed movie.',
        'A dramatic story about love.',
        'A light-hearted comedy.',
        'Action with a twist.'
    ]
})

# Step 2: Create TF-IDF Matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(items['Description'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Step 3: Make Recommendations
def content_based_recommendations(movie_title):
    idx = items.index[items['Movie'] == movie_title][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Get top 3
    movie_indices = [i[0] for i in sim_scores]
    return items['Movie'].iloc[movie_indices].tolist()

# Example usage of Content-Based Filtering
print("\nContent-Based Recommendations for 'Movie A':")
print(content_based_recommendations("Movie A"))
