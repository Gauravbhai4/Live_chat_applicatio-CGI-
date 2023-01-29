import socket
server=socket.socket()
server_ip=input('enter server ip:\n')
server_port=12345
server.bind((server_ip,server_port))
server.listen()
print(f'server is running on {server_ip}:{server_port}')
client,addr=server.accept()
client_ip,client_port=addr
print('got a connection from client')
print(f'client addres is{client_ip} :{client_port}')

last="bye"

while True:
    request=client.recv(1024).decode()
    print(f"client request {request}".rjust(100))
    if request.lower()==last:
        print('server is closed by  client side')
        break

    msg=input('enter message to send: ').encode()
    client.send(msg)
    if msg.lower()==last:
        print('closing connection form server side')
        client.close()
        break
    server.close()