# sources: class textbook and project 1

import socket

def main():
    host = 'localhost'
    port = 12344
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print(f'Connected to: {host} on port: {port}')

    try:

        print('type /q to quit')
        while True:
            # get a message from the user
            message = input('Enter your message: ')

            if message == '/q':
                break
            # Send the message to the server
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f'Server replied: {data.decode()}')
    finally:
        # close  socket
        s.close()

if __name__ == '__main__':
    main()
