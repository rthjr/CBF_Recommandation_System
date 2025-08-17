CBF standfor Content-based filtering, it is a recommendation system technique that focuses on the characteristics of the items themselves, rather than user interactions with those items.

** HOW IT WORKS **


IT is a simple recommendation system that takes user input (a course interest) and recommends similar subject and url of the course based on their titles. 
It uses the TF-IDF (Term Frequency-Inverse Document Frequency) technique to convert text data into numerical vectors and calculates the cosine similarity 
between the user input and all course titles to find the most similar ones.

* let's break down each line of the code:

* import pandas as pd: Imports the Pandas library and assigns it the alias pd.

* from sklearn.feature_extraction.text import TfidfVectorizer: Imports the TfidfVectorizer class from the scikit-learn library,
  which is used to convert a collection of raw documents to a matrix of TF-IDF features.
  
* from sklearn.metrics.pairwise import cosine_similarity: Imports the cosine_similarity function from scikit-learn, which calculates the cosine similarity between vectors.

* data = pd.read_csv('filtering_course.csv'): Reads the CSV file named filtering_course.csv into a Pandas DataFrame named data.

* data['Title'] = data['Title'].fillna(''): Fills missing values in the 'Title' column with empty strings.

* data['Title'] = data['Title'].str.lower(): Converts all strings in the 'Title' column to lowercase.

* tfidf_vectorizer = TfidfVectorizer(): Initializes a TF-IDF Vectorizer object.

* tfidf_matrix = tfidf_vectorizer.fit_transform(data['Title']): Fits the TF-IDF Vectorizer to the 'Title' column and transforms the text data into TF-IDF features, storing the result in tfidf_matrix.

* def recommend_course(user_input, top_n=5):: Defines a function named recommend_course that takes user input and an optional parameter top_n (default value is 5) to specify the number of recommended courses.

* user_input = user_input.lower(): Converts the user input to lowercase.

* user_tfidf = tfidf_vectorizer.transform([user_input]): Transforms the user input into TF-IDF features using the same TF-IDF Vectorizer.

* cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten(): Calculates the cosine similarity between the user input and all course titles, 
 flattens the result, and stores it in cosine_similarities.

* top_indices = cosine_similarities.argsort()[-top_n:][::-1]: Gets the indices of the top top_n most similar courses based on cosine similarity.

* recommendations = data.iloc[top_indices][['Title', 'URL']]: Retrieves the recommended courses (titles and URLs) from the DataFrame using the top indices.

* return recommendations: Returns the recommended courses.

* user_input = input("Enter your course interest: "): Prompts the user to enter their course interest and stores the input in user_input.

* recommendations = recommend_course(user_input): Calls the recommend_course function with the user input and stores the result in recommendations.

* print("Recommended Courses:"): Prints a message indicating that the recommended courses will be displayed.

* for i, (title, url) in enumerate(zip(recommendations['Title'], recommendations['URL']), start=1):: Loops through the recommended courses using enumerate to get both the index (i) 
 and the corresponding title and URL.

* print(f"{i}: {title} {url}"): Prints the index, title, and URL of each recommended course in the specified format.
<!-- thank you -->