class card:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class actionCard(card):
    def __init__(self, name, cost):
        super(actionCard, self).__init__(name, cost)

class equipCard(card):
    def __init__(self, name, cost):
        super(equipCard, self).__init__(name, cost)

