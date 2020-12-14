# ENTITY MODULE
""" Module responsible for establishing the framework of inheritance and methods of entities (player characters & monsters) 
    used throughout the main program.
"""

import random
import copy

def roll_die(dice_amount, dice_range):
    """ Serves as a "virtual die roller", establishing a range and randomly selecting an amount of numbers determined by the input.
    
    Parameters
    ----------
    dice_amount : int
        integer taken from [0] value of referenced dictionary, determines total amount of numbers selected
    dice_range : int
        integer taken from [1] value of referenced dictionary, provides extent of range
    
    Returns
    -------
    output : int
        integer that represents the sum of numbers randomly selected
    """
    list_range = range(1, dice_range+1)
    dice_counter = 0
    output = 0
    while dice_counter < dice_amount:
        output += random.choice(list_range)
        dice_counter += 1
    return output
    
class Entity():   
    """ Primary class providing the framework for all entities to interact with one another, basis for both player 
        characters and monsters.
        
    Attributes
    ----------
    health : int
        integer that represents the health of the entity
    attacks : dict
        dictionary referencing availaible "attacks" for entity
    starting_attacks : dict
        dictionary that maintains a copy of the default (starting) values of entity attacks
    starting_potions : dict
        dictionary that maintains a copy of the default (starting) values of entity potions
    potions : dict
        dictionary referencing available "potions" for entity
    max_health : int
        integer that represents the total maximum health assigned to the entity, provides an upper limit
    """
    # default for health of entity
    health = 0 
    
    # default for dictionary of "attacks" for entity, structure for each set up as {basic attack, 
    # heavy attack, 'ultimate' attack}
    attacks = {}
    starting_attacks = {}
    starting_potions = {}
    
    # default for dictionary of "potions" for entity, structure for each set up as {lesser potion, 
    # greater potion, superior potion}
    potions = {}
    
    # "upper limit" of health for entity, prevents adding health from healing potions
    max_health = 0 
    def __init__(self, name, health):
        """ Class constructor for Entity class.
        Parameters
        ----------
        name : string
            string determining the "name" of the entity
        health : int
            integer determining the "health value" of the entity
        """
        self.name = name
        self.health = health
        self.max_health = health
        
        # "deep copy" format modified from: https://stackoverflow.com/questions/5105517/deep-copy-of-a-dict-in-python
        self.starting_attacks = copy.deepcopy(self.attacks)
        self.starting_potions = copy.deepcopy(self.potions)
    
    def attack(self, input_attack, target):
        """ Processes user input for an "attack" choice, as well as calculating and distributing the appropriate "damage". 
    
        Parameters
        ----------
        input_attack : string
            string either provided by user or chosen for the monster, provides the name for the 
            relevant key within the attacks dictionary
        target : object
            object that points the total sum of "damage" from the input attack to be distributed to the respective entity (player, enemy)
            
        Returns
        -------
        output : bool
            bool returns True if the input attack is valid, returns False otherwise
        """
        # checks to make sure the input string is actually a key available in the "attacks" dictionary
        # makes use of roll_die function to "calculate damage"
        # subtracts target's health from damage of attack
        # finally reduces the number of uses available by one
        if input_attack in self.attacks.keys(): 
            current_attack = self.attacks[input_attack]
            if current_attack[-1] != 0: 
                damage = roll_die(current_attack[0], current_attack[1])
                print(self.name + ' dealt ' + str(damage) + ' damage to ' + target.name + ' with ' + input_attack + '.')
                target.health -= damage
                current_attack[-1] -= 1
                return True
            
            # print statement for using an attack that has 0 uses left
            else:
                print(self.name + ' tried to use ' + input_attack + ', but appears fatigued! (no uses left)' ) 
                
        return False
    
    def heal(self, input_potion):
        """ Processes user input for a "potion" choice, as well as caculating and distributing appropriate "healing".

        Parameters
        ----------
        input_potion : string
            string provided by user, provides the name for the relevant key within the potions dictionary
            
        Returns
        -------
        output : bool
            bool returns True if the input attack is valid, returns False otherwise
        """
        # heal function works similarly to the attack function above, references "potions" dictionary
        if input_potion in self.potions.keys(): 
            current_potion = self.potions[input_potion]
            if current_potion[-1] != 0:
                healing = roll_die(current_potion[0], current_potion[1])
                print(self.name + ' healed ' + str(healing) + ' health back using a ' + input_potion + '.')
                self.health += healing
                if self.health >= self.max_health:
                    self.health = self.max_health
                current_potion[-1] -= 1
                return True
            else:
                print(self.name + ' tried to use a ' + input_potion + ', but has none of that type left!')
        
        return False
    
    def inventory(self):
        """ Prints out the referenced "attacks" and "potions" dictionaries assigned to the entity.
        """
        # prints out the inventory of the current entity (info on attacks and potions, format denoted below) 
        # {attack_name : [die amount, die value, uses avaialble]}
        # {potion_name : [die amount, die value, uses avaialble]}
        print('')
        print('Format of inventory follows: {\'name of input\' : [\'die\' amount, \'die\' value, uses available]}')
        print('Attacks:')
        print('--------')
        print(self.attacks) 
        print('')
        print('Potions:')
        print('--------')
        print(self.potions)
  
    def reset_attacks(self):
        """ Sets referenced attacks dictionary back to original default values. 
        """
        # sets self.attacks to the starting default values of the attacks dictionary for that entity
        self.attacks = copy.deepcopy(self.starting_attacks)
    
    def reset_all(self):
        """ Sets referenced attacks and potions dictionaries back to original default values. 
        """
        # sets self.attacks and self.potions to the starting default values of their respective dictionaries for a given entity
        self.attacks = copy.deepcopy(self.starting_attacks)
        self.potions = copy.deepcopy(self.starting_potions)