socket = new WebSocket(
  window.location.protocol == 'http'
    ? 'ws://'
    : 'ws://' + window.location.host + '/'
)
socket.onopen = function open() {
  console.log('WebSockets connection created.')
  socket.send('Hola! Echo!')
}

socket.onmessage = function(event) {
  console.log(event.data)
}
