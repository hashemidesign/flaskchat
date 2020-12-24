from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_super_secret_key'
app.config['DEBUG'] = True
s_io = SocketIO(app)

users = {}


@app.route('/')
def home():
    return render_template('index.html')


from sockets import *


if __name__ == '__main__':
    s_io.run(app, port=5500)
