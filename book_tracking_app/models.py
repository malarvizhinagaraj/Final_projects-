from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100))
    isbn = db.Column(db.String(20))
    progress = db.Column(db.Integer, default=0)
    rating = db.Column(db.Integer)
    review = db.Column(db.Text)
    genre = db.Column(db.String(50))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

class Lending(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    borrower = db.Column(db.String(100))
    date_lent = db.Column(db.DateTime, default=datetime.utcnow)
    returned = db.Column(db.Boolean, default=False)

class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    author = db.Column(db.String(100))
    notes = db.Column(db.Text)

class ReadingChallenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.Integer)
    progress = db.Column(db.Integer)
