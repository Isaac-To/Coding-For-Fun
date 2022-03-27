import socket
import datetime
from multiprocessing.dummy import Process
import json

def listen(s):
    while True:
    #listen to server
        jsonified_message = s.recv(1024).decode('utf-8')
        message = json.loads(jsonified_message)
        if message['room'] == curroom:
            output_msg = f"{message['author']}@{message['time']}: {message['content']}"
            print(output_msg)

def respond(s):
    global curroom
    curroom = 'general'
    while True:
    #response to server on message sent
        curtime = datetime.datetime.now().strftime('%Y/%m/%d:%H:%M:%S')
        message = input('')
        #all commands will start with /
        if message.startswith('/'):
            command = message.replace('/', '')
            if command == 'quit':
                respondProcess.close()
                quit()
            if command == 'room':
                curroom = input('Input your desired room: ')
                print(f'[+] Succeeded in switching room to {curroom}')
        else: #if not a command
            complete_message = dict(
                author=USERNAME,
                room=curroom,
                time=curtime,
                content=message
            )
            jsonified_message = json.dumps(complete_message)
            s.send(jsonified_message.encode('utf-8'))

if __name__ == "__main__":
    #get user information
    USERNAME = input('Enter your username: ')

    #create a socket
    while True:
        try:
            hostname = input('What is the server hostname you wish to connect to: ').split(':')
            SERVER_HOST = hostname[0]
            SERVER_PORT = int(hostname[1])
            break
        except:
            print('[-] Invalid hostname. Enter as SERVER_IP/HOSTNAME:PORT')
    del hostname
    print(f'Connecting to server {SERVER_HOST}:{SERVER_PORT}')
    try:
        s = socket.socket()
        s.connect((SERVER_HOST, SERVER_PORT))
    except socket.error:
        input(f'There has been an error connecting to {SERVER_HOST}:{SERVER_PORT}; Press enter to retry')
    #start and run Processes
    listenProcess = Process(target=listen, args=(s,))
    respondProcess = Process(target=respond, args=(s,))
    listenProcess.start()
    respondProcess.start()