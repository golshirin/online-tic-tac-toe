from client import Client
from threading import Thread
from constants import *


def __main__():
    client = Client()
    thread = Thread(target=client.start(SERVER_HOST, SERVER_PORT))
    while True:
        print("***************\n"
              "1. Connect to server\n"
              "2. Exit\n"
              "***************")
        choice = input("Enter your choice: ")
        if choice == "1":
           thread.start()
        elif choice == "2":
            client.stop()
            break


if __name__ == "__main__":
    __main__()
