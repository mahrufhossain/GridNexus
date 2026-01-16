# models/marketplace.py

class CentralController:
    def __init__(self, neighbors):
        self.neighbors = neighbors

    def find_trade_opportunities(self):
        sellers = [n for n in self.neighbors if n.get_net_energy() > 0]
        buyers = [n for n in self.neighbors if n.get_net_energy() < 0]
        return sellers, buyers