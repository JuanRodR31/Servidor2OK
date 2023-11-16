import socket
clientSocket = socket.socket()
clientSocket.bind (('localhost', 8000))
clientSocket.listen(5)

while True:
    conexion ,direccion = clientSocket.accept()
    print("nueva conexion establecida")
    print(direccion)

    peticion=conexion.recv(1024)
    print(peticion)

    conexion.send(b"hola desde el servidor")
    conexion.close()