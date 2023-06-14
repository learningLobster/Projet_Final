import pygame
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory

class GameClientProtocol(Protocol):
    def connectionMade(self):
        print("Connexion établie au serveur")
        self.transport.write("Hello, server!".encode())

    def dataReceived(self, data):
        received_data = data.decode()
        print("Réponse du serveur :", received_data)
        self.transport.loseConnection()

    def connectionLost(self, reason):
        print("Connexion perdue")

class GameClientFactory(ClientFactory):
    protocol = GameClientProtocol

    def clientConnectionFailed(self, connector, reason):
        print("Échec de la connexion au serveur :", reason.getErrorMessage())
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connexion perdue :", reason.getErrorMessage())
        reactor.stop()

if __name__ == '__main__':
    reactor.connectTCP("localhost", 8000, GameClientFactory())
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                reactor.stop()
