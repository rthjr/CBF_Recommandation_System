import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


data = pd.read_csv('filtered_course.csv')

# preprocess the data
data['Title'] = data['Title'].fillna('')
data['Title'] = data['Title'].str.lower()

# initialize TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()

# transform the TF-IDF Vectorizer
tfidf_matrix = tfidf_vectorizer.fit_transform(data['Title'])

def recommend_course(user_input, top_n=5):
    # user input
    user_input = user_input.lower()
    
    # transform user input using the same TF-IDF Vectorizer
    user_tfidf = tfidf_vectorizer.transform([user_input])

    # calculate cosine similarity between user input and all titles
    cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten()

    # get indices of top N most similar courses
    top_indices = cosine_similarities.argsort()[-top_n:][::-1]

    # top N recommended courses
    recommendations = data.iloc[top_indices][['Title', 'URL']]
    return recommendations


user_input = input("Enter your course interest: ")
recommendations = recommend_course(user_input)
print("Recommended Courses:")
for i, (title, url) in enumerate(zip(recommendations['Title'], recommendations['URL']), start=1):
    print(f"{i}: {title} {url}")
