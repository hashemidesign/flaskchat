from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_super_secret_key'
app.config['DEBUG'] = True
s_io = SocketIO(app)

users = {}


@app.route('/')
def home():
    return render_template('index.html')


@s_io.on('message')
def received_message(message):
    send('hi client. Im here...')
    print(message)


@app.route('/originate')
def originate():
    s_io.emit('server originated', 'something happened on the server')
    return '<h1>sent!</h1>'


@s_io.on('message from user', namespace='/messages')
def receive_message_from_user(message):
    print(message)
    emit('from flask', message.upper(), broadcast=True, namespace='/')


@s_io.on('username', namespace='/private')
def receive_username(username):
    # users.append({username: request.sid})
    users[username] = request.sid
    print('user name added')


@s_io.on('private_message', namespace='/private')
def private_message(payload):
    recipient_session_id = users[payload['username']]
    message = payload['message']

    emit('new_private_message', message, room=recipient_session_id)


@s_io.on('join_room', namespace='/private')
def handle_join_room(room):
    print(room)
    join_room(room)
    emit('room_message', 'a new user has joined!', room=room)


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
