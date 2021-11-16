"""
Chapitre 11.1

Classes pour représenter un personnage.
"""

import random
import utils

UNARMED_POWER = 20


class Weapon:
	UNARMED_POWER = UNARMED_POWER
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	def __init__(self, name, power, min_level = 1):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self):
		return self.__name

		
	def make_unarmed():
		return Weapon("Unarmed", UNARMED_POWER)
	


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, name, max_hp, attack, defense, level, weapon = None):
		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.hp = max_hp

		if weapon == None:
			self.weapon = Weapon.make_unarmed()

	@property
	def name(self):
		return self.__name

	def compute_damage(attacker, defender):
		crit = random.choices([1, 2], [100 - 6.25, 6.25])
		modifier = crit[0] * random.randint(85, 100) / 100
		
		damages = ((2 * attacker.level / 5 + 2) * attacker.weapon.power * attacker.attack / defender.defense / 50 + 2) * modifier
		defender.hp = max(0, defender.hp - damages)

		return int(damages)


def deal_damage(attacker, defender):
	# Calculer dégâts
	print(f"{attacker.name} used {attacker.weapon.name}")
	if defender.hp > 0:
		print("  Critical hit!")
	print(f"  {defender.name} took {Character.compute_damage(attacker, defender)} dmg")

def run_battle(c1, c2):
	turns = 0
	attacker, defender = c1, c2
	print(f"{attacker.name} starts a battle with {defender.name}!")

	while True:
		deal_damage(attacker, defender)
		if defender.hp <= 0:
			print(f"{defender.name} is sleeping with the fishes.")
			break
		attacker, defender = defender, attacker
		turns += 1
		
	return turns
