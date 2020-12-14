import pytest
from Characters import Barbarian, Ranger
from Monsters import Goblin

def test_class_attacks():
    test = "Great Sword"
    test_2 = "Arrow Rain"
    test_3 = "Wooden Sword"
    assert test in Barbarian.attacks.keys()
    assert test not in Ranger.attacks.keys()
    assert test_2 in Ranger.attacks.keys()
    assert test_3 not in Barbarian.attacks.keys()
    assert test_3 in Goblin.attacks.keys()

def test_health_and_name():
    test = Barbarian("Test Barbarian", 90)
    test_2 = Goblin("Test Goblin", 75)
    assert test.health == 90
    assert test_2.health == 75
    assert test.name == "Test Barbarian"
    assert test_2.name == "Test Goblin"
    
def test_attack_damage():
    test_player = Barbarian("Test Player", 1)
    test_target = Goblin("Test Goblin", 25)
    test_player.attack("Short Sword", test_target)
    print(test_target.health, test_target.max_health)
    assert test_target.health < test_target.max_health
    
def test_healing():
    test_player = Barbarian("Test Player", 25)
    test_attacker = Goblin("Goblin", 1)
    test_attacker.attack("Shield Bash", test_player)
    assert test_player.health != test_player.max_health
    test_player.heal("Greater Health Potion")
    assert test_player.health == test_player.max_health