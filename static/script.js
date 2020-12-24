$(document).ready(function () {
    let socket = io.connect('http://127.0.0.1:5500');

    $('#send').on('click', function() {
        let message = $('#message').val();

        socket.emit('message from user', message);
    }); // end on click function

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