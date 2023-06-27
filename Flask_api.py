from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Dummy data
books = [
    {
        'id': 1,
        'title': 'Book 1',
        'author': 'Author 1'
    },
    {
        'id': 2,
        'title': 'Book 1',
        'author': 'Author 1'
    },

]

# Book resource
class BookResource(Resource):
    def get(self, book_id=None):
        if book_id is None:
            return books, 200
        book = [book for book in books if book['id'] == book_id]
        if len(book) == 0:
            return {'error': 'Book not found'}, 404
        return book[0], 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('author', type=str, required=True)
        args = parser.parse_args()
        new_book = {
            'id': len(books) + 1,
            'title': args['title'],
            'author': args['author']
        }
        books.append(new_book)
        return new_book, 201

    def put(self, book_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('author', type=str, required=True)
        args = parser.parse_args()
        book = [book for book in books if book['id'] == book_id]
        if len(book) == 0:
            return {'error': 'Book not found'}, 404
        book[0]['title'] = args['title']
        book[0]['author'] = args['author']
        return book[0], 200

    def delete(self, book_id):
        book = [book for book in books if book['id'] == book_id]
        if len(book) == 0:
            return {'error': 'Book not found'}, 404
        books.remove(book[0])
        return {'message': 'Book deleted'}, 200

# API routes
api.add_resource(BookResource, '/books', '/books/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)
