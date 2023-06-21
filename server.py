# sources: class textbook and my project 1

import socket

def main():

    host = 'localhost'
    port = 12344
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    print(f'Server listening on: {host} on port: {port}')

    # accept an incoming connection
    conn, addr = s.accept()
    print(f'Connected to {addr}')
    print('Type /q to quit')

    try:

        while True:
            # receive data from the client
            data = conn.recv(1024)
            # If no data is received, break the loop
            if not data:
                break

            message = data.decode()
            print(f'Received: {message}')
            # get a reply from the client
            reply = input('Enter your reply: ')

            # If the reply is '/q' break loop
            if reply == '/q':
                break
            # send the reply back to client
            conn.sendall(reply.encode())
    finally:
        # close the connection and the socket
        conn.close()
        s.close()

if __name__ == '__main__':
    main()
