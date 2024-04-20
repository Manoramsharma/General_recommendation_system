import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class HackathonRecommender:
    def __init__(self, hackathon_data_file):
        """
        Initialize the recommender system with the hackathon dataset.
        """
        self.data = pd.read_csv(hackathon_data_file)
        self.skills_vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        self.interests_vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        
        # Assuming 'Required Skills' and 'Interests' columns exist in the dataset
        self.data['skills_tfidf'] = self.skills_vectorizer.fit_transform(self.data['Required Skills'])
        self.data['interests_tfidf'] = self.interests_vectorizer.fit_transform(self.data['Interests'])
        
    def recommend(self, user_profile):
        """
        Recommend hackathons based on the user's profile.
        """
        user_skills_vec = self.skills_vectorizer.transform([user_profile['skills']])
        user_interests_vec = self.interests_vectorizer.transform([user_profile['interests']])
        
        skills_similarity = cosine_similarity(user_skills_vec, self.data['skills_tfidf']).flatten()
        interests_similarity = cosine_similarity(user_interests_vec, self.data['interests_tfidf']).flatten()
        
        # Combining the similarity scores
        combined_similarity = (skills_similarity + interests_similarity) / 2
        
        # Sorting the hackathons based on combined similarity score
        top_indices = combined_similarity.argsort()[::-1]
        recommended_hackathons = self.data.iloc[top_indices]
        
        return recommended_hackathons.head(10)  # return top 10 recommendations

# Example usage:
# Create an instance of the recommender system with the path to your hackathon dataset CSV
# recommender = HackathonRecommender('path_to_hackathon_data.csv')

# Define a user profile with their skills and interests
# user_profile = {
#     'skills': 'Python;Data Science',
#     'interests': 'Machine Learning;AI'
# }

# Get recommendations
# recommendations = recommender.recommend(user_profile)
# print(recommendations)
