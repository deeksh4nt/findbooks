from flask import Flask, Response, request
from recommendation import recommend

app = Flask(__name__)

@app.route('/')
def root():
  return "Provide ISBN value to get recommendations <br>Example <ul><li><a href=\"9780007136582\">/</a></li></ul>", 400

@app.route('/<int:book>')
def find_books(book):
  try:
    page = request.args.get('page', default=1, type=int)
    books = recommend(book, page)
    result = [str(b) for b in books]
    return Response('\n'.join(result), mimetype='text/plain')
  except:
    return Response('invalid request', mimetype='text/plain')
