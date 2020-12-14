# MONSTERS MODULE
""" Module responsible for establishing the framework of monster entities, specifically assigning unique "attacks"
    dictionaries used throughout the main program.
"""
# proper import structure modified from: 
# https://stackoverflow.com/questions/46130977/module-init-takes-at-most-2-arguments-3-given-when-creating-instance-o

from Entity import Entity 

class Goblin(Entity):
    """ Class representing the "Goblin" monster.
    Attributes
    ----------
    attacks : dict
        dictionary referencing unique attacks for Goblin monster.
    """
    def __init__(self, name, health):
        """ Class constructor for Goblin class.
        Parameters
        ----------
        name : string
            string determining the "name" of the monster
        health : int
            integer determining the "health value" of the monster
        """
        super().__init__(name, health)
        
    # "attacks" dictionary for the specific entity, format follows {attack_name : [die amount, die value, uses avaialble]}
    attacks = {'Shield Bash' : [1, 6, 10],
               'Long Bow' : [2, 4, 3],
               'Wooden Sword' : [2, 6, 1]}

class SkeletonWarrior(Entity):
    """ Class representing the "Skeleton Warrior" monster.
    Attributes
    ----------
    attacks : dict
        dictionary referencing unique attacks for Skeleton Warrior monster.
    """
    def __init__(self, name, health):
        """ Class constructor for Skeleton Warrior class.
        Parameters
        ----------
        name : string
            string determining the "name" of the monster
        health : int
            integer determining the "health value" of the monster
        """
        super().__init__(name, health)
    attacks = {'Riposte' : [2, 4, 10],
               'Haunting Gaze' : [3, 4, 3],
               'Grave Slash' : [4, 4, 1]}

class Minotaur(Entity):
    """ Class representing the "Minotaur" monster.
    Attributes
    ----------
    attacks : dict
        dictionary referencing unique attacks for Minotaur monster.
    """
    def __init__(self, name, health):
        """ Class constructor for Minotaur class.
        Parameters
        ----------
        name : string
            string determining the "name" of the monster
        health : int
            integer determining the "health value" of the monster
        """
        super().__init__(name, health)
    attacks = {'Greataxe' : [3, 4, 10],
               'Gore Rush' : [4, 4, 3],
               'Trample' : [4, 5, 1]}
    
class Chimera(Entity):
    """ Class representing the "Chimera" monster.
    Attributes
    ----------
    attacks : dict
        dictionary referencing unique attacks for Chimera monster.
    """
    def __init__(self, name, health):
        """ Class constructor for Chimera class.
        Parameters
        ----------
        name : string
            string determining the "name" of the monster
        health : int
            integer determining the "health value" of the monster
        """
        super().__init__(name, health)
    attacks = {'Tail Swipe' : [3, 4, 10],
               'Claw' : [4, 4, 3],
               'Vicious Bite' : [5, 5, 1]}
    
class Dragon(Entity):
    """ Class representing the "Dragon" monster.
    Attributes
    ----------
    attacks : dict
        dictionary referencing unique attacks for Dragon monster.
    """
    def __init__(self, name, health):
        """ Class constructor for Dragon class.
        Parameters
        ----------
        name : string
            string determining the "name" of the monster
        health : int
            integer determining the "health value" of the monster
        """
        super().__init__(name, health)
    attacks = {'Body Slam' : [4, 4, 10],
               'Claw' : [4, 5, 3],
               'Flame Breath' : [6, 5, 1]}