import socket
import threading  


class Server:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connections = []
        self.threads = []
        self.running = True
        self.game_over = True
        self.name = []

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        print ('socket binded to post', self.port)
        self.server.listen(2)
        print ('socket is listening...')
        for i in range(10):
            client, addr = self.server.accept() 
            print('Connected to :', addr[0], ':', addr[1]) 
            threading.Thread(target=self.handle, args=(client,addr)).start() 

        self.server.close()

    def handle(self, client, addr):
        try:
            while self.game_over: 
                self.data = client.recv(1024)

                if self.data == b'n':
                    client.sendall(self.data)
                    print('OK bye player by Conncetion to', addr[0], ':', addr[1], 'lost.')
                    break
                elif self.data == b'y':
                    client.sendall(self.data)
                    self.data = client.recv(1024)
                    if self.name == []:
                        self.name.append(self.data)
                        self.message = 'Please wait for the next player'
                        client.sendall(self.message.encode('ascii'))
                    else:
                        self.name.append(self.data)
                        print(self.name[0],self.name[1])
                        import game
                        
                else:
                    client.sendall(b'Wrong entry!') 

            client.close()

        except Exception as e:
            print(e)
            print("SERVER: Connection closed: " + str(addr))
            self.connections.remove(client)
            self.threads.remove(Thread(target=self.handle, args=(client, addr)))
            client.close()

    def stop(self):
        self.running = False
        for conn in self.connections:
            client.close()
        for thread in self.threads:
            thread.join()
        self.socket.close()

    def send_all(self, data):
        for conn in self.connections:
            client.send(data)

    def get_connections(self):
        return self.connections
