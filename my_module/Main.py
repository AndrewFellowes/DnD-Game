# Structure for parsing input used throughout, modified from: 
# https://stackoverflow.com/questions/14907067/how-do-i-restart-a-program-based-on-user-input

import Entity
import Monsters
import Characters
import time
import random

# Idea for "quitting" out of the script taken from: 
# https://stackoverflow.com/questions/543309/programmatically-stop-execution-of-python-script
from sys import exit

# used primarily for restart capability
game_start = True 
while game_start:
    while True:
        
        # user input for desired name
        player_name = str(input('Hello! First, please input the name you would like to have: '))
        while True: 
            player_name_confirm = str(input('Your name will be ' + player_name + '.' + ' Is this correct?(Y/N)'))
            if player_name_confirm in ('Y', 'N'):
                break
            print('Invalid input.')
        if player_name_confirm == 'N':
                continue
        if player_name_confirm == 'Y':
            print('Welcome, ' + player_name + ' to my final project for COGS 18 FA20, a D&D inspired text-game!')
            break

    print('Next you will need to pick a class, your options are: Barbarian, Ranger, or Wizard.')  
    player_class_options = ['Barbarian', 'Ranger', 'Wizard']
    while True:
        
        # user input for desired class
        player_class = str(input('Please input the class you would like to play: '))
        if player_class in player_class_options:
            while player_class in player_class_options:
                player_class_confirm = input('Very good! So you will be ' + player_name + ' the ' + player_class + '.' + ' Is this correct?(Y/N)')
                if player_class_confirm in ('Y', 'N'):
                    break
                print('Invalid input. Please input \'Y\' or \'N\'.')
            if player_class_confirm == 'N':
                continue
            if player_class_confirm == 'Y':
                print('Alright, ' + player_name + ' the last thing to do is pick a difficulty.')
                break
        else:
            print('Please enter a correct class: \'Barbarian\', \'Ranger\', or \'Wizard\'.')

    print('The difficulty options are: Easy, Medium, and Hard.')
    print('NOTE: The difficulty of the game scales quite high, I would recommend starting on Easy to see the entire program run first.')
    difficulty_options = ['Easy', 'Medium', 'Hard']
    while True:
        
        # user input for desired difficulty
        difficulty_choice = str(input('Please input the difficulty you would like to play on: '))
        if difficulty_choice in difficulty_options:
            while difficulty_choice in difficulty_options:
                difficulty_confirm = input('You have chosen to play on ' + difficulty_choice + '.' + ' Is this correct?(Y/N)')
                if difficulty_confirm in ('Y', 'N'):
                    break
                print('Invalid input.')
            if difficulty_confirm == 'N':
                continue
            if difficulty_confirm == 'Y':
                print('And so the adventure begins with our hero, ' + player_name + '...')
                break
        else:
            print('It seems you did not enter a correct difficulty option, try again!')
            print('Again your options are: \'Easy\', \'Medium\', or \'Hard\'')

    # Class setup: performs backend of assigning the appropriate class from Characters module based on user input
    # uses player_name from the input above and sets health value
    if player_class == 'Barbarian': 
        player = Characters.Barbarian(player_name, 90) 
    elif player_class == 'Ranger':
        player = Characters.Ranger(player_name, 75)
    else:
        player = Characters.Wizard(player_name, 65)

    # Difficulty selection: determines total amount of encounters, starts game on stage 1
    if difficulty_choice == 'Easy':
        total_stages = 1
    elif difficulty_choice == 'Medium':
        total_stages = 3
    else:
        total_stages = 5

    current_stage = 1
    
    # Variable that keeps track of turn order (0 = player, 1 = enemy)
    turn_counter = 0
        
    # Resets the player's inventory completely to default values for both attacks and potions
    # primarily for restarting the game properly
    player.reset_all()
    
    while current_stage <= total_stages:
    
        # Assigns the correct monster to "enemy" variable based on the current stage of the game
        # also sets appropriate name and health value
        if current_stage == 1:
            enemy = Monsters.Goblin('Goblin', 25)
            
            # Reset function solely for setting attacks to default values
            enemy.reset_attacks()
            print('As you wander the ruins of the fallen kingdom, suddenly debris shifts in the distance.')
            print('The dust settles, and standing before you is a small Goblin creature.')
        elif current_stage == 2:
            enemy = Monsters.SkeletonWarrior('Skeleton Warrior', 35)
            enemy.reset_attacks()
            print('Pressing onward into the castle\'s dungeon, the air is still and quiet.')
            print('Eerie rattling can be overheard in the distance, and as you continue walking a Skeleton Warrior emrerges.')
            print('The undead creature blocks your path!')
        elif current_stage == 3:
            enemy = Monsters.Minotaur('Minotaur', 55)
            enemy.reset_attacks()
            print('Taking a moments rest you collect yourself and begin the descent to the heart of the dungeon.')
            print('Rumor of treasure has filled your mind, as you continue to walk further.')
            print('Cautiously pacing the inner sanctum of the castle ruins, loud stomps can be overheard just slightly out of earshot.')
            print('The stomps grow ever louder and ultimately you find its source... a great Minotaur guards the treasure!')
        elif current_stage == 4:
            enemy = Monsters.Chimera('Chimera', 65)
            enemy.reset_attacks()
            print('Recovering from the Minotaur you finally make it to the treasure chest...')
            print('But as you approach it a shadowy figure begins drifting along your periphery.')
            print('A roar of a lion pierces your ears as a great monstrosity emerges from the shadows.')
            print('A beast of mythical proportions carefully watches your movements, you recognize this strange creature as a Chimera!')
        elif current_stage == 5:
            enemy = Monsters.Dragon('Dragon', 75)
            enemy.reset_attacks()
            print('You stand back for a moment reeling from the continuous battles thus far.')
            print('After much trial and tribulation you manage to succesfully reclaim the treasure.')
            print('The only task remaining in your way is to find a way out... perhaps the main entry way is still open?')
            print('Rushing toward your freedom... just as the sun once again sets on your face a harsh wind blows in your direction.')
            print('Heavy wingbeats continue to assault your senses, you recoil in horror as what lays before you comes into view.')
            print('A colossal Red Dragon abruptly slams into the ground, fury and anger fill its eyes.') 
            print('You have a sudden realization that this treasure was being guarded by the legendary creature.')
            print('Brushing yourself off, there is only one way forward.')
        
        # Primary combat loop
        while player.health > 0 and enemy.health > 0:
            if turn_counter == 0:
                
                # Player input for action to perform on their turn
                player_turn = str(input('It\'s your turn, would you like to Attack, Heal, or Check Inventory?'))
                if player_turn not in ('Attack', 'Heal', 'Check Inventory'):
                    print('Invalid input. Please input \'Attack\', \'Heal\', or \'Check Inventory\'.')
                    continue
                    
                # Input for attack to use
                if player_turn == 'Attack':
                    print('Your attack choices are',list(player.attacks.keys()))
                    input_attack = str(input('Which attack would you like to use?'))
                    if input_attack in (list(player.attacks.keys())):
                        attack_use_counter = player.attacks[input_attack]
                        print('You attack with ' + input_attack + '! (' + str(attack_use_counter[-1]-1) + ' uses left)')
                        player.attack(input_attack, enemy)
                        print('The ' + enemy.name + ' currently has ' + str(enemy.health) + ' health.')
                    else:
                        print('Invalid input. Make sure to check the spelling and spacing of the input attack.')
                        continue
                        
                # Input for potion to use        
                elif player_turn == 'Heal':
                    if player.health != player.max_health:
                        print('Your potion choices are',list(player.potions.keys()))
                        input_potion = str(input('Which potion would you like to use?'))
                        if input_potion in (list(player.potions.keys())):
                            potion_use_counter = player.potions[input_potion]
                            print('You used a ' + input_potion + '. (' + str(potion_use_counter[-1]-1) + ' remaining)')
                            player.heal(input_potion)
                            print('You currently have ' + str(player.health) + '(' + str(player.max_health) + ')' + ' health.')
                        else:
                            print('Invalid input. Make sure to check the spelling and spacing of the input potion.')
                            continue
                    else: 
                        print('You are currently at max health and do not need to heal.')
                        continue
                
                # Input to check player inventory (Attack/Potion Uses)
                elif player_turn == 'Check Inventory':
                    player.inventory()
                    continue
                    
            # Code that handles enemy turn
            else:
                turn_counter == 1
                enemy_action = print('The ' + enemy.name + ' strikes!')
                
                # If the enemy tries to use an attack with no uses left it will roll again, 
                # although still possible to "miss"
                for i in range(2):
                    input_attack = (random.choice(list(enemy.attacks.keys())))
                    if(enemy.attacks[input_attack][-1] != 0):
                        break
                enemy.attack(input_attack, player)
                print('You currently have ' + str(player.health) + '(' + str(player.max_health) + ')' + ' health.')
            turn_counter = (turn_counter + 1) % 2
        
        # End of combat if enemy dies first
        if enemy.health <= 0:
            print('Great job! You succesfully defeated the ' + enemy.name + '.')
            
            # Game end code, checks if max stages are completed based on difficulty selected
            if current_stage == total_stages:
                print('Congratulations, you have beaten all stages for ' + difficulty_choice + '!')
                print('If you would like, now try a harder difficulty for more monsters.')
                break
                    
            # If there are more stages left the game will keep going, user may choose to 'rest' between stages
            # resting sets attack values to default
            else:
                rest_input = str(input('Would you like to rest and recharge your abilities before the next stage?(Y/N)'))
                if rest_input == 'Y':
                    print('Resting...')
                    player.reset_attacks()
            current_stage +=1

        # End of combat if player dies first
        else:
            print('And so the hero fell in battle on stage ' + str(current_stage) + '. Slain by the ' + enemy.name + '.')
            print('Feel free to try again if you would like!')
            break
                
    # Input allowing user to restart the game back to beginning (user name input)
    game_restart = str(input('Would you like to restart the game?(Y/N)'))
    if game_restart == 'Y':
        print('The game will restart in 3 seconds.')
        time.sleep(3)
                   
    # Closes the game
    else:
        print('Thank you for playing my game! It will automatically close in 3 seconds.')
        time.sleep(3)
        exit("\'Main.py\' script has been stopped. Please execute the script again if you wish to run it.")
