let socket = io.connect('http://127.0.0.1:5500');

socket.on('connect', function() {
    socket.send('page is now connected');
});