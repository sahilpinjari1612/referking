from flask import Flask, render_template, request, redirect, session, url_for, flash
import sqlite3
import json
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_folder='static')
app.secret_key = 'your_secret_key'  # Change this in production


# Initialize user database
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL)''')
    conn.commit()
    conn.close()


# Home page – only visible to logged-in users
@app.route('/')
def home():
    if 'username' not in session:
        return redirect('/login')
    
    try:
        with open('data/offers.json') as f:
            offers = json.load(f)
    except Exception as e:
        print("Error loading offers:", e)
        offers = []
    return render_template('index.html', offers=offers)


# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        try:
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
                      (username, email, password))
            conn.commit()
            conn.close()
            flash('Registered successfully! Please login.')
            return redirect('/login')
        except sqlite3.IntegrityError:
            flash('Username already exists!')
            return redirect('/register')

    return render_template('register.html')


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = c.fetchone()
        conn.close()

        if result and check_password_hash(result[0], password):
            session['username'] = username
            return redirect('/')
        else:
            flash('Invalid credentials')
            return redirect('/login')

    return render_template('login.html')


# Dashboard (optional)
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"Welcome {session['username']}! You are logged in."
    return redirect('/login')


# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully.')
    return redirect('/login')


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
