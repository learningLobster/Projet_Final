from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor
from GUI import Game


class GameProtocol(Protocol):
    def connectionMade(self):
        print("Nouvelle connexion")
        self.transport.write("Bienvenue sur le serveur de jeu !".encode())

    def dataReceived(self, data):
        received_data = data.decode()
        print("Données reçues du client :", received_data)

        if received_data == "START":
            # Le client a cliqué sur le bouton "start"

            # Préparez le plateau de jeu
            game_board = Game.show_board()  # Fonction à implémenter pour générer le plateau de jeu

            # Envoie du plateau de jeu au client
            response = str(game_board)  # Convertit le plateau de jeu en une chaîne de caractères pour l'envoi
            self.transport.write(response.encode())

        else:
            response = "Commande non valide"
            self.transport.write(response.encode())


factory = Factory()
factory.protocol = GameProtocol
SERVER_PORT = 8000
reactor.listenTCP(SERVER_PORT, factory)
reactor.run()
