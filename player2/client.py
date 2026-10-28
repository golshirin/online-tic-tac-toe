import socket
import threading

class Client:

    def __init__(self):
        self.running = True

    def start(self, host, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        threading.Thread(target=self.handle, args=(client,)). start() 
        
        
         
        
    def handle(self, client):
        try:
            while self.running:
                self.message_ready = input("Are you ready to play?(y/n):");
                client.sendall(self.message_ready.encode('ascii')) 
                if self.message_ready == 'n':
                    break
                self.data = client.recv(1024)
                if self.data == b'y':
                    self.message_user = input("Enter your username:");
                    client.sendall(self.message_user.encode('ascii'))
                
                self.data = client.recv(1024)
                print(self.data.decode('ascii'))
            client.close()
                 
        except Exception as e:
            print(e)
            self.running = False
            #self.client.close()

            
    def stop(self):
        self.running = False
        client.close()

    def send(self, data):
        self.client.send(data)

    def receive(self):
        return self.client.recv(1024)
