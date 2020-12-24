from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_super_secret_key'
app.config['DEBUG'] = True
s_io = SocketIO(app)


@app.route('/')
def home():
    return render_template('index.html')


@s_io.on('message')
def received_message(message):
    print(message)


if __name__ == '__main__':
    s_io.run(app, port=5500)
