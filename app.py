from flask import Flask, render_template, redirect, url_for, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

@app.route('/')
def home():
    if 'logged_in' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'karthik' and password == '0214':  # Replace with actual username/password
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('home'))
        elif username == 'maha' and password == '0214':
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return 'Invalid credentials, please try again.'

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Updated to listen on all network interfaces
