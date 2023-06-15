import socket

# Adresse IP et port du serveur
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8000

# Connexion au serveur
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))

# Envoi de la commande "START" au serveur
sock.sendall("START".encode())

# Réception de la réponse du serveur (le plateau de jeu)
response = sock.recv(1024).decode()
print("Plateau de jeu reçu :", response)

# Fermeture de la connexion
sock.close()
