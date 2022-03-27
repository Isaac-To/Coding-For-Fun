import socket
from multiprocessing.dummy import Process, Pool

import settings
def listen(c):
    while True:
        try:
            msg = c.recv(1024).decode('utf8')
        except Exception as e:
            print('[!] Error:', e)
            clients.remove(c)
            return
        sendPool = Pool()
        sendPool.map(lambda x: x.send(msg.encode('utf8')), clients)

def close():
    print('[!] Server closed', clients)
    for c in clients:
        c.close()

def accept():
    #accept all incomming connections
    (client, client_address) = s.accept()
    print(f'[+] {client_address[0]} connected to server')
    clients.add(client)
    list_Processes.append(Process(target=listen, args=(client,)))
    list_Processes[-1].start()

if __name__ == "__main__":
    clients = set()
    s = socket.socket()

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((settings.host, settings.port))
    s.listen(100)
    print(f'Server started s.on {settings.host}:{settings.port}')

    #this is for storing all the listen Processs
    list_Processes = []
    while True:
        accept()

# close server socket
#close()
s.close()