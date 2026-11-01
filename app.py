
from flask import Flask, jsonify, request

app = Flask(__name__)

# Data buku menggunakan Local Array
books = [
    {
        "id": 1,
        "title": "Laskar Pelangi",
        "author": "Andrea Hirata",
        "year": 2005,
        "stock": 4
    },
    {
        "id": 2,
        "title": "Bumi Manusia",
        "author": "Pramoedya Ananta Toer",
        "year": 1980,
        "stock": 3
    }
]

# GET semua buku
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books), 200


# GET detail buku berdasarkan ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book), 200

    return jsonify({"error": "Book not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)
