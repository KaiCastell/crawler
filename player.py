import entity

class Player(entity.Entity):
    equipment = [] # any time you add an equipment/trait/relic you add to the actions or conditions dictionary/list
    traits = []
    relics = [] #includes normal and taxes
    #REPLACEME Conditions 2D List?
    xp = 0
    xpMult = 1.0
    block = 0
    blockMult = 1.0
    critChance = 0.05 # base is 5% but can change
    critDmgMult = 2.0 # base is a damage double
    healingMult = 1.0
    dmgInMult = {'all':1.0, 'bludgeoning':1.0, 'slashing':1.0, 'piercing':1.0, 'magic':1.0, 'fire':1.0, 'cold':1.0, 'electric':1.0, 'poison':1.0} #works like a multiplier table. 0.5 is a 50% resistance. dictionary lookup is better here
    dmgOutMult = {'all':1.0, 'bludgeoning':1.0, 'slashing':1.0, 'piercing':1.0, 'magic':1.0, 'fire':1.0, 'cold':1.0, 'electric':1.0, 'poison':1.0}
    luck = {'common':0.50, 'uncommon':0.30, 'rare':0.15, 'epic':0.04, 'legendary':0.01} # REPLACEME this is a placeholder because i don't know all the interactables, but it should turn out to be an array of chances one for each interaction that can be affected by relics, e.g. luck to find rare items is normally 2% and can be upped
    def __init__(self, user, maxHealth, health, speed):
        self.user = user
        self.maxHealth = maxHealth
        self.health = health #current health. Should almost always initialize to = max health
        self.speed = speed
    def __str__(self):
        return f"Player: {self.user}\n"+ super(Player, self).__str__() + f"Luck:\n{self.luck}\nXP: {self.xp}\nXP Multiplier: {self.xpMult}\nActions:\n{self.actions}\nEquipment:\n{self.equipment}\nTraits:\n{self.traits}\nRelics:\n{self.relics}\n"

class Doctor(Player):
    def __init__(self, user):
        super().__init__(user, 65, 65, 3)
        # add doctor equipment and traits once that's a thing. adding these will automatically affect actions and stats? 
    def __str__(self):
        return "**Doctor**\n" + super(Doctor, self).__str__()
    
class Scientist(Player):
    def __init__(self, user):
        super().__init__(user, 60, 60, 2) # just different values for now just for sake's sake
        # add doctor equipment and traits once that's a thing. adding these will automatically affect actions and stats?
    def __str__(self):
        return "**Scientist**\n" + super(Scientist, self).__str__()