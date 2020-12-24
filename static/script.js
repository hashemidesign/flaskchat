let socket = io.connect('http://127.0.0.1:5500');

socket.on('connect', function() {
    socket.send('page is now connected');

    socket.emit('custom event', 'The custom event message');
});

socket.on('message', function (message) {
    console.log(message);
});

socket.on('from flask', function (message) {
    console.log(message);
});