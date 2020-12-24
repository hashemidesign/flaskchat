$(document).ready(function () {
    let socket = io.connect('http://127.0.0.1:5500');
    // using namespace to group particular messages
    let socket_messages = io.connect('http://127.0.0.1:5500/messages');

    let private_socket = io.connect('http://127.0.0.1:5500/private');

    $('#send').on('click', function() {
        let message = $('#message').val();

        socket_messages.emit('message from user', message);
    }); // end on click function

    $('#send_username').on('click', function () {
        let username = $('#username').val();
        private_socket.emit('username', username);
    });

    $('#send_private_message').on('click', function () {
        let recipient = $('#send_to_username').val();
        let message = $('#send_to_message').val();
        private_socket.emit('private_message', {'username': recipient, 'message': message});
    });

    $('#join_room').on('click', function () {
        let room = $('#room_to_join').val();
        private_socket.emit('join_room', room);
    });

    private_socket.on('new_private_message', function(message) {
        console.log(message);
    });

    private_socket.on('room_message', function(message) {
        console.log(message);
    });


    socket.on('from flask', function(message) {
        console.log(message);
    });

    socket.on('server originated', function(message) {
        console.log(message);
    });


    /*

    socket.on('connect', function () {

        socket.send('page is now connected');

        socket.emit('custom event', 'The custom event message');
        socket.emit('json event', {'name': 'Mohsen'})

        socket.on('message', function (message) {
            console.log(message);
        });

        socket.on('from flask', function (message) {
            console.log(message);
        });

        socket.on('from flask that received json', function (message) {
            console.log(message['extension']);
        });

    }); // end socket on connection

     */
}); // end ready function