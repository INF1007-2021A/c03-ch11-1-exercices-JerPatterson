"""
Chapitre 11.1

Classes pour représenter un personnage.
"""

import random
import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	UNARMED_POWER = 20

	def __init__(self, name, power, min_level = 1):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self):
		return self.__name

	@classmethod	
	def make_unarmed(cls):
		return cls("Unarmed", cls.UNARMED_POWER)
	


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
		self.__weapon = weapon

		if self.__weapon == None:
			self.weapon = Weapon.make_unarmed()

	@property
	def name(self):
		return self.__name

	@property
	def weapon(self):
		return self.__weapon

	@weapon.setter # Pour que le test fonctionne
	def weapon(self, value):
		self.__weapon = value
		if self.__weapon == None:
			self.__weapon = Weapon.make_unarmed()

	def compute_damage(self, defender: 'Character'):
		crit = random.choices([1, 2], [100 - 6.25, 6.25])
		crit = (crit, crit == 1)
		modifier = crit[0][0] * random.randint(85, 100) / 100
		
		damages = ((2 * self.level / 5 + 2) * self.weapon.power * self.attack / defender.defense / 50 + 2) * modifier
		defender.hp = max(0, defender.hp - damages)

		return int(damages), crit[1]


def deal_damage(attacker: 'Character', defender: 'Character'):
	# Calculer dégâts
	damages, critical = attacker.compute_damage(defender)
	print(f"{attacker.name} used {attacker.weapon.name}")
	if critical:
		print("  Critical hit!")
	print(f"  {defender.name} took {damages} dmg")

def run_battle(c1: 'Character', c2: 'Character'):
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
