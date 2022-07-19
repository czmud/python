from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import book
from flask_app.models import favorite


@app.route('/books/')
def view_all_books():
    books = book.Book.get_all()
    return render_template("books.html", books=books)
@app.route('/books/<int:book_id>')
def show_book(book_id):
    data = { "id": book_id }
    books = book.Book.get_book_by_id(data)
    return render_template("bookshow.html", books=books)
@app.route('/create_book/', methods=["POST"])
def create_book():
    data = {
        "title": request.form["title"],
        "num_of_pages": request.form["num_of_pages"]
    }
    book.Book.save(data)
    return redirect('/books')
@app.route('/add_book_favorite', methods=["POST"])
def add_book_favorite():
    data = {
        "user_id": request.form["user_id"],
        "book_id": request.form["book_id"]
    }
    favorite.Favorite.save(data)
    return redirect('books/'+data['book_id'])