# Online Tic-Tac-Toe 🎮

A multiplayer online Tic-Tac-Toe (Dooz) game built with Python using socket programming.

This project includes a server and two clients (Player 1 and Player 2) that can play against each other over the network.

---

## Project Structure

online-tic-tac-toe/
├── server/          # Server side code
├── player1/         # Client for Player 1
└── player2/         # Client for Player 2


---

## How to Run the Game

### 1. Start the Server
Open a terminal and run:

```bash
cd server
python start_server.py

2. Start Player 1
Open another terminal and run:

cd player1
python start_client.py

3. Start Player 2
Open a third terminal and run:

cd player2
python start_client.py

Requirements

Python 3.x
No external libraries required (uses built-in socket module)


Notes

Make sure the server is running before starting the clients.
Both players should be connected to the same network (or use localhost for testing on one computer).