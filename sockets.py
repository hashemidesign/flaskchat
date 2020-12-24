from flask import request
from flask_socketio import send, emit, join_room, disconnect

from app import s_io, users, app


@app.route('/originate')
def originate():
    s_io.emit('server originated', 'something happened on the server')
    return '<h1>sent!</h1>'


@s_io.on('message')
def received_message(message):
    send('hi client. Im here...')
    print(message)


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


# on_connect & on_disconnect are useful for authentication!
@s_io.on('connect', namespace='/private')
def on_connect():
    print('connection established')


@s_io.on('disconnect', namespace='/private')
def on_disconnect():
    print('connection ended')


@s_io.on('disconnect_me', namespace='/private')
def disconnect_me(msg):
    disconnect()


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