import time, socket, sys
print('Client server...')
time.sleep(1)
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostname(shost)
print(shost, '({}'.format(ip))
server_host = input('enter server\'s IP address:')
name = input('enter client name: ')
port = 1234
print('trying to connect to server:{}, ({})'.format(server_host, port))
time.sleep(1)
soc.connect((server_host, port))
print("connected...\n")
soc.send(name.encode())
server_name = soc.recv(1024)
server_name = server_name.decode()
print('{} has joined...'.format(server_name))
print('enter [bye] to exit')
while True:
    message = soc.recv(1024)
    message = message.decode()
    print(server_name, ">", message)
    message = input(str("Me >"))
    if message == "[bye]":
        message = "leaving chat"
        soc.send(message.encode())
        print("\n")
        break
    soc.send(message.encode())
