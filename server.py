import socket
import threading
from encryption_utils import EncryptionManager
from user_auth import UserAuthentication
from quiz_questions import NBAQuizQuestions

class NBAQuizServer:
    def __init__(self, host='127.0.0.1', port=65432):
        """
        [Socket Programming] Initialize NBA Quiz Server
        
        Args:
            host (str): Server host
            port (int): Server port
        """
        # [Socket Programming] Creating server socket
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        
        # [Lists and Dictionaries] Player scores dictionary
        self.player_scores = {}

    def start_server(self):
        """
        [Socket Programming] Start the server and listen for connections
        [Loops] Continuous loop to accept client connections
        """
        # [Loops] Infinite loop to accept connections
        self.server_socket.listen()
        print(f"NBA Quiz Server started on {self.host}:{self.port}")
        
        while True:
            # [Socket Programming] Accept client connections
            client_socket, address = self.server_socket.accept()
            # [Threading] Create a new thread for each client
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

def main():
    """
    [Functions] Main function to start the server
    """
    server = NBAQuizServer()
    server.start_server()

if __name__ == "__main__":
    main()
