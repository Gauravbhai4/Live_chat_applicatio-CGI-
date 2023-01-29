import socket
client=socket.socket()
server_ip=input('enter server ip:')
server_port=12345
client.connect((server_ip,server_port))
print(f'connected to server{server_ip}{server_port}')

last ='bye'
while True:    
    request=input('enter message to send: ').encode()
    client.send(request)
    if request.lower()==last:
        print('connection closed by client')
        break
    response=client.recv(1024).decode()
    #decode to string
    print(f"server = {response}".rjust(100))
    if response.lower()==last:
        print('connection close by server')
        break
client.close()