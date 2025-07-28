import requests

def fetch_book_info(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    res = requests.get(url)
    return res.json()

def genre_statistics(books):
    stats = {}
    for book in books:
        genre = book.genre
        if genre:
            stats[genre] = stats.get(genre, 0) + 1
    return stats

def export_books(books):
    return [book.__dict__ for book in books]

def import_books(data, db, Book):
    for entry in data:
        book = Book(**entry)
        db.session.add(book)
    db.session.commit()
