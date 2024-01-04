import pandas, pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pandas.read_csv('training_data')

training_data = data[['isbn13', 'description']].copy()

training_data['description'] = data['title'] + ' ' + data['authors'] + ' ' + data['description'] + ' ' + data['categories']
training_data['description'].fillna('', inplace=True)

tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(training_data['description'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

training_data.to_csv('output_data', index=False)
pickle.dump(cosine_sim, open('cosine_matrix', 'wb'))
