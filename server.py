from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor

class GameProtocol(Protocol):
    def connectionMade(self):
        print("Nouvelle connexion")
        self.transport.write("Bienvenue sur le serveur de jeu !".encode())

    def dataReceived(self, data):
        received_data = data.decode()
        print("Données reçues du client :", received_data)

        # Répondre au client
        response = "J'ai reçu votre message : {}".format(received_data)
        self.transport.write(response.encode())

    def connectionLost(self, reason):
        print("Connexion perdue")

class GameFactory(Factory):
    def buildProtocol(self, addr):
        return GameProtocol()

if __name__ == '__main__':
    reactor.listenTCP(8000, GameFactory())
    print("Serveur démarré sur le port 8000")
    reactor.run()
