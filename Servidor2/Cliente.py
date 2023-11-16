import socket

clientSocket = socket.socket()
clientSocket.connect(('localhost', 8000))
clientSocket.send(b"hola desde el cliente")
respuesta = clientSocket.recv(1024)
print (respuesta)

clientSocket.close()