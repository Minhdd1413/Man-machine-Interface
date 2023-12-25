from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import openai

app = Flask(__name__)
@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/home')
def home():
    return render_template('home.html')
if __name__ == '__main__':
    app.run()
