# CHARACTERS MODULE
""" Module responsible for establishing the framework of player character entities, specifically assigning unique "attacks"
    and "potions" dictionaries used throughout the main program.
"""
# proper import structure modified from: 
# https://stackoverflow.com/questions/46130977/module-init-takes-at-most-2-arguments-3-given-when-creating-instance-o
from Entity import Entity

class Barbarian(Entity):
    """ Class representing the "Barbarian" player class.
    Attributes
    ----------
    attacks : dict
        dictionary referencing unique attacks for Barbarian player class.
    potions : dict
        dictionary referencing unique potions for Barbarian player class.
    """
    # "attacks" dictionary for the specific entity, format follows {attack_name : [die amount, die value, uses avaialble]}
    attacks = {'Short Sword' : [2, 6, 10],
               'Great Sword' : [3, 6, 4],
               'Reckless Blow' : [3, 8, 1]}
    
    def __init__(self, name, health):
        """ Class constructor for Barbarian class.
        Parameters
        ----------
        name : string
            string determining the "name" of the player character
        health : int
            integer determining the "health value" of the player character
        """
        super().__init__(name, health)
    
    # "potions" dictionary for the specific entity, format follows {potion_name : [die amount, die value, uses avaialble]}
    potions = {'Lesser Health Potion' : [4,6,3],
               'Greater Health Potion' : [5,7,3],
               'Superior Health Potion' : [8,5,2]}

class Ranger(Entity):
    """ Class representing the "Ranger" player class.
    Attributes
    ----------
    attacks : dict
        dictionary referencing unique attacks for Ranger player class.
    potions : dict
        dictionary referencing unique potions for Ranger player class.
    """
    attacks = {'Short Bow' : [2, 8, 10],
               'Heavy Crossbow' : [3, 8, 4],
               'Arrow Rain' : [4, 8, 1] }
  
    def __init__(self, name, health):
        """ Class constructor for Ranger class.
        Parameters
        ----------
        name : string
            string determining the "name" of the player character
        health : int
            integer determining the "health value" of the player character
        """
        super().__init__(name, health)
    
    potions = {'Lesser Health Potion' : [4,6,3],
               'Greater Health Potion' : [5,7,3],
               'Superior Health Potion' : [8,5,2]}

class Wizard(Entity):
    """ Class representing the "Wizard" player class.
    Attributes
    ----------
    attacks : dict
        dictionary referencing unique attacks for Wizard player class.
    potions : dict
        dictionary referencing unique potions for Wizard player class.
    """
    attacks = {'Energy Bolt' : [3, 6, 10],
               'Magic Missile' : [4, 7, 4],
               'Fireball' : [8, 4, 1],
               'Test' : [1000, 1, 1]}
    
    def __init__(self, name, health):
        """ Class constructor for Wizard class.
        Parameters
        ----------
        name : string
            string determining the "name" of the player character
        health : int
            integer determining the "health value" of the player character
        """
        super().__init__(name, health)
    
    potions = {'Lesser Health Potion' : [4,6,3],
               'Greater Health Potion' : [5,7,3],
               'Superior Health Potion' : [8,5,2]}