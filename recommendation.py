import pickle
import pandas

MAX_ITEMS = 10

data = pandas.read_csv("output_data")
cosine_matrix = pickle.load(open("cosine_matrix", "rb"))

def recommend(book, page=1):
  book_index = data[data['isbn13'] == book].index.tolist()[0]

  sim_scores = list(enumerate(cosine_matrix[book_index]))
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

  page = max(1, page)
  start = (page-1) * MAX_ITEMS + page
  end = start + MAX_ITEMS

  sim_scores = sim_scores[start:end]
  book_indices = [i[0] for i in sim_scores]

  return data['isbn13'].iloc[book_indices].tolist()
