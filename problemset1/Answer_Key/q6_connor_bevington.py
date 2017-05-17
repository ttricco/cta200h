import numpy as np
import time

class Ship(object):

    def __init__(self, laser, name, shield=25., hull=25.):
        self.shield = shield   # shield strength: 50 intially
        self.hull   = hull     # hull strength: 50 initially
        self.laser  = laser    # laser power: between 1 and 10
        self.name   = name     # ship name
        
        if self.laser > 10 or self.laser < 1:
            # must have a laser power between 1 and 10
            raise ValueError("laser power must be between 1 and 10")
    
    # check if ship is destroyed
    def is_destroyed(self, index):
        if self.hull <= 0:     # ship is destroyed when hull has a non-positive strength
            print("{} has been destroyed!!!\n".format(self.name)) # print to log
            del players[index] # delete this player from the game
    
    # how to handle when a player is shot
    def shot(self, attacker, index):
        if attacker.__class__ == Warship and np.random.rand() < 0.3:
            # allow for double power via missile in warships 30% of the time
            missile = 1 
        else:
            missile = 0
        if self.__class__ == Speeder and np.random.rand() < 0.5:
            # speeders dodge incoming shots 50% of the time
            print("{} has dodged {}'s shot!\n".format(self.name, attacker.name))
        elif self.shield > 0: # if shield strength available, deplete it first
            # shield depletes by full laser power, or double power if missile
            self.shield -= attacker.laser * (1 + missile)
            print("{}'s shields have been hit with a power {} attack by {}! Their shield strength is now {}.\n".format(self.name, \
            attacker.laser * (1 + missile), attacker.name, max(self.shield,0)))
        else: # shield strength is 0, so hull is depleted
            # hull depletes by half laser power or missile power
            self.hull -= 0.5*(attacker.laser * (1 + missile))
            print("{}'s hull has been hit with a power {} attack by {}! Their hull strength is now {}.\n".format(self.name, \
            attacker.laser * (1 + missile), attacker.name, max(self.hull,0)))
        # check if attacked ship is destroyed by the most recent attack
        self.is_destroyed(index)
    
    # how to handle a ship that fires a shot
    def shoot(self, players):
        # choose a random target amongst the players
        index = np.random.randint(0,high=len(players))
        target = players[index]
        if target.name != self.name: # ensure they do not shoot themselves!
            print("{} has shot at {}!".format(self.name, target.name))
            # shot has been fired, so pass to shot function to determine outcome
            target.shot(self, index)
            
class Warship(Ship):
    
    pass # interit from ship


class Speeder(Ship):
    
    pass # interit from ship

""" DESIGNING BATTLE """

# ships
Feynman = Ship(10,'Feynman')
Sagan = Ship(9, 'Sagan')
Newton = Ship(8, 'Newton')

# warship
Tesla = Warship(7, 'Tesla')

# speeder
Einstein = Speeder(2, 'Einstein')

players = [Feynman, Sagan, Newton, Tesla, Einstein]

# function to initiate battle
def battle(players, fast=False):
    
    # print introduction to game
    print("\nWelcome to the great Physics battle! Today's battle is between \
{}, {}, {}, {}, and {}. Players fire at random in an attempt to destroy \
each other's ships. Last one standing wins!\n".format(players[0].name, \
    players[1].name, players[2].name,players[3].name,players[4].name))
    
    time.sleep(5) # allow for user to read
    
    print("The battle starts in 3...") # initiate countdown
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...\n")
    time.sleep(1)

    while len(players) > 1: # simulate until one player left
        # choose a random player to fire a shot
        index = np.random.randint(0,len(players))
        players[index].shoot(players)
        if not fast: # if just wanting to view results, change to fast=True
            time.sleep(0.5)
            
    # upon completion of battle, delcare the victor in the log
    print("\n{} has won the battle with a hull strength of {} to spare!!! \
    ".format(players[0].name, players[0].hull))

# initiate the battle!
battle(players)
    
