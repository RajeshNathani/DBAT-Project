from unicodedata import name
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from db import connectBooks, connectUsers, addUsers
app = Flask(__name__)

app.secret_key = "secret"

@app.route('/')
def home():
    books = connectBooks()
    return render_template('index.html', len = len(books), books=books)

@app.route('/books')
def books():
    books = connectBooks()
    return render_template('books.html', len = len(books), books=books)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        users = connectUsers()
        for i in users:
            if i[2] == username and i[3] == password:
                return redirect(url_for('home'))
            else:
                flash('Invalid Credentials. Please try again.')
                return redirect(url_for('login'))

    users = connectUsers()
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        users = connectUsers()
        for i in users:
            if i[2] == email:
                flash('Email already exists. Please try again.')
                return redirect(url_for('register'))
        else:
            addUsers(name, email, password)
            flash('You are now registered and can log in.')
            return redirect(url_for('login'))

    return render_template('register.html')



@app.route('/books/<int:book_id>')
def book(book_id):
    books = connectBooks()
    for i in books:
        if i[0] == book_id:
            book_name = i[1]
            book_author = i[2]
            book_description = i[3]
            book_quantity = i[4]
            book_image = i[5]
            return render_template('books.html', book_name=book_name, book_author=book_author, book_description=book_description, book_image=book_image, book_quantity=book_quantity)


@app.route('/logout')
def logout():
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)