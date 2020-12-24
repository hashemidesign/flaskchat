from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_super_secret_key'
app.config['DEBUG'] = True
s_io = SocketIO(app)


@app.route('/')
def home():
    return render_template('index.html')


@s_io.on('message')
def received_message(message):
    send('hi client. Im here...')
    print(message)


@s_io.on('message from user')
def receive_message_from_user(message):
    print(message)
    emit('from flask', message.upper(), broadcast=True)


'''
@s_io.on('custom event')
def receive_custom_event(message):
    print(f'THE CUSTOM MESSAGE EMITTED FROM JS: {message}')
    emit('from flask', 'this is from server emit')


@s_io.on('json event')
def receive_json_event(message):
    print(f'THE CUSTOM MESSAGE EMITTED FROM JSON: {message["name"]}')
    emit('from flask that received json', {'extension': 'flask socket io'})
'''


if __name__ == '__main__':
    s_io.run(app, port=5500)
