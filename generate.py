import random #random.choice
import copy #copy.copy
import re

class MinionAbility:
	templates = [
		{'value': 0.00, 'text': '<ability>.' },
		{'value': 0.20, 'text': 'Battlecry: <effect>.'},
		{'value': 0.20, 'text': 'Battlecry: <targetable_effect>.'},
		{'value': 0.20, 'text': 'Battlecry: If <condition>, <targetable_effect>.'},
		{'value': 0.30, 'text': 'Battlecry: If <condition>, <targetable_effect> and <effect>.'},
		{'value': 0.50, 'text': 'Battlecry: Gain <stackable_effect> for every spell in your hand.'},
		{'value': 0.50, 'text': 'Battlecry: Gain <stackable_effect> for every minion in your hand.'},
		{'value': 0.20, 'text': 'Deathrattle: <effect>.'},
		{'value': 0.50, 'text': 'Inspire: <effect>.'},
		{'value': 0.50, 'text': 'At the beginning of your turn, <effect>.'},
		{'value': 0.50, 'text': 'At the end of your turn, gain <ability>.'},
		{'value': 0.50, 'text': 'At the end of each turn, <effect>.'},
		{'value': 0.20, 'text': 'Combo: <effect>.'},
		{'value': 0.20, 'text': 'Combo: <targetable_effect>.'},
		{'value': 0.70, 'text': 'Your <minion_type>s are <minion_type>s.'},
		{'value': 0.70, 'text': 'Your <minion_type>s gain <stackable_effect>.'},
		{'value': 0.70, 'text': 'Your <minion_type>s gain <ability>.'},

	]

	effects = [
		{'value': 1.84, 'text': 'Draw a card'},
		{'value': 1.00, 'text': 'Draw <V+(2-4)> cards'},
		{'value': -1.25, 'text': 'Discard a card'},
		{'value': -1.98, 'text': 'Your opponent draws a card'},
		{'value': -0.27, 'text': 'Deal <q+(1-10)> damage to your hero'},
		{'value': 0.75, 'text': 'Equip a random weapon'},
		{'value': 1.31, 'text': 'Your other minions gain <stackable_effect>'},
		{'value': 1.31, 'text': 'Your <minion_type>s gain <stackable_effect>'},
		{'value': 0.31, 'text': 'Gain <stackable_effect> for every <minion_type> in your hand'},
		{'value': 0.31, 'text': 'Give a random friendly minion <ability>'},
		{'value': 0.31, 'text': 'Gain <ability> until end of turn'},

	]

	conditions = [
		{'value': -5.0, 'text': 'your deck has no more than 1 of any card' },
		{'value': -0.40, 'text': 'your deck has at least <i+(2-20)> <minion_type>s'},
		{'value': -0.40, 'text': 'your deck has no more than <i+(2-20)> <minion_type>s'},
		{'value': 0.00, 'text': 'you have at least <i+(2-8)> cards in hand'}
	]

	targetable_effects = [
		{'value': 0.82, 'text': 'Deal <v+(0-8)> damage to a minion'},
		{'value': 0.82, 'text': 'Deal <v+(1-6)> damage to an enemy'},
		{'value': 1.84, 'text': 'Deal <V+(0-8)> damage to all enemy minions'},
		{'value': 5.33, 'text': 'Destroy a minion'},
		{'value': 2.73, 'text': 'Destroy a <minion_type>'},
		{'value': 1.02, 'text': 'Freeze a minion'},
		{'value': 0.42, 'text': 'Freeze a <minion_type>'},
		{'value': 0.83, 'text': 'Silence a minion'},
		{'value': 0.13, 'text': 'Silence a <minion_type>'},
		{'value': 1.05, 'text': 'Discover a <minion_type>'},
	]

	stackable_effects = [
		{'value': 0.57, 'text': '+<v+(1-5)> Attack'},
		{'value': 0.40, 'text': '+<v+(1-5)> Health'},
		{'value': 1.10, 'text': '+<v+(1-5)>/+<v+(1-5)>'},
		{'value': 0.46, 'text': 'Spell Power +1'},
	]

	abilities = [
		{'value': 0.51, 'text': 'Taunt'},
		{'value': 1.40, 'text': 'Divine Shield'},
		{'value': 1.19, 'text': 'Windfury'},
		{'value': 0.46, 'text': 'Spell Power +<v+(1-3)>'},
		{'value': 0.33, 'text': 'Charge'},
		{'value': 0.61, 'text': 'Stealth'},
		{'value': -0.83, 'text': 'Overload (<i+(1-3)>)'}
	]

	minion_types = [
		'beast', 'dragon', 'murloc', 'demon', 'mech'
	]

	def __init__(self, text="", value=0):
		#print("MinionAbility init with text=%s & value=%s" % (text, value))
		self.text = text
		self.value = value

	@staticmethod
	def random():
		#print("Generating random minion ability")

		ability = copy.copy(random.choice(MinionAbility.templates))
		#print("Chose template %s" % ability)

		while '<effect>' in ability.get('text'):
			random_effect    = random.choice(MinionAbility.effects)
			ability['text']  = ability['text'].replace('<effect>', random_effect.get('text'), 1)
			ability['value'] = ability['value'] + random_effect.get('value')

		while '<targetable_effect>' in ability.get('text'):
			random_effect    = random.choice(MinionAbility.targetable_effects)
			ability['text']  = ability['text'].replace('<targetable_effect>', random_effect.get('text'), 1)
			ability['value'] = ability['value'] + random_effect.get('value')

		while '<stackable_effect>' in ability.get('text'):
			random_effect    = random.choice(MinionAbility.stackable_effects)
			ability['text']  = ability['text'].replace('<stackable_effect>', random_effect.get('text'), 1)
			ability['value'] = ability['value'] + random_effect.get('value')

		while '<condition>' in ability.get('text'):
			condition        = random.choice(MinionAbility.conditions)
			ability['text']  = ability['text'].replace('<condition>', condition.get('text'), 1)
			ability['value'] = ability['value'] + condition.get('value')

		while '<ability>' in ability.get('text'):
			random_ability   = random.choice(MinionAbility.abilities)
			ability['text']  = ability['text'].replace('<ability>', random_ability.get('text'), 1)
			ability['value'] = ability['value'] + random_ability.get('value')

		# Replace variable rolls
		while True:
			match = re.search('\<(\w*)\+*\((\d+)\-(\d+)\)\>', ability.get('text'))
			if not match:
				break

			flags, lower_bound, upper_bound = match.group(1), match.group(2), match.group(3)

			roll = random.randint(int(lower_bound), int(upper_bound))
			#print("Rolled %s for %s in %s" % (roll, match.group(0), ability.get('text')))

			if False: pass     # Flags defined below:
			elif 'v' in flags: # increase value by the roll amount
				ability['value'] = ability['value'] + roll
			elif 'V' in flags: # increase value by 2 times the roll amount
				ability['value'] = ability['value'] + 2 * roll
			elif 'i' in flags: # decrease value by the roll amount
				ability['value'] = ability['value'] - roll
			elif 'q' in flags: # decrease value by 0.25 * roll around
				ability['value'] = ability['value'] - 0.25 * roll
			elif 'm' in flags: # multiply ability times roll
				ability['value'] = ability['value'] * roll

			# Do the text substitution
			ability['text'] = re.sub('\<(\w*)\+*\((\d+)\-(\d+)\)\>', str(roll), ability.get('text'), count=1)

		# Replace minion types
		while '<minion_type>' in ability.get('text'):
			random_type      = random.choice(MinionAbility.minion_types)
			ability['text']  = ability['text'].replace('<minion_type>', random_type, 1)

		#print("Built ability: %s" % ability)

		return MinionAbility(text=ability.get('text'), value=ability.get('value'))

class Card:
	def __init__(self):
		self.name = "Unnamed card"

	def generate_abilities(self):
		raise Exception("must implement generate_abilities in Card subclass")

	def ability_value(self):
		#print("Calculating cost")
		total_cost = sum([ability.value for ability in self.abilities])
		return total_cost

	def __str__(self):
		return "%s (%s), %s/%s %s %s: %s" % (
			self.name,
			self.cost,
			self.attack,
			self.health,
			self.hero,
			self.card_type,
			' '.join([ability.text for ability in self.abilities])
		)

	def to_csv(self):
		return "%s;%s;%s;%s;%s;%s;%s" % (
			self.name,
			self.cost,
			self.attack,
			self.health,
			self.hero,
			self.card_type,
			' '.join([ability.text for ability in self.abilities])
		)

class MinionCard(Card):
	value_per_attack_point = 0.57
	value_per_health_point = 0.40

	name_prefaces = [
		'Holy', 'Dark', 'Merchant', 'Lively'
	]

	names = [
		'Knight', 'Soldier', 'Adventurer', 'Commander'
	]

	name_suffixes = [
		'of Dragons', 'of the Moon', 'of love'
	]

	def __init__(self):
		#print("Minion init")
		self.card_type = 'minion'
		self.hero = 'neutral'
		self.generate_name()
		self.generate_abilities()
		self.generate_stats()
		self.sanity_check_edges()

	def generate_name(self):
		self.name = ' '.join([
			random.choice(MinionCard.name_prefaces),
			random.choice(MinionCard.names),
			random.choice(MinionCard.name_suffixes)
		])

	def generate_abilities(self):
		#print('Generating minion abilities')
		self.abilities = []

		number_of_abilities = 1 #random.randint(1, 2)
		for a in range(0, number_of_abilities):
			self.abilities.append(MinionAbility.random())

	def generate_stats(self):
		#print('Generating minion stats')

		ability_value = self.ability_value()
		#print("Beginning with %s ability value" % ability_value)
		if ability_value >= 10:
			self.cost   = 10
			self.attack = random.randint(0, 1)
			self.health = 1
			return

		extra_value = random.uniform(0, 10 - ability_value)
		#print("Adding %s extra value in stats" % extra_value)

		attack_value_distribution = random.uniform(0.01, extra_value)
		self.attack = int(attack_value_distribution / MinionCard.value_per_attack_point)

		health_value_distribution = extra_value - attack_value_distribution
		self.health = int(health_value_distribution / MinionCard.value_per_health_point)

		self.cost = int(ability_value + extra_value)

	def sanity_check_edges(self):
		if self.cost < 0:
			self.cost = 0
		elif self.cost > 10:
			self.cost = 10

		if self.health < 1:
			self.health = 1


print('Name;Cost;Attack;Health;Class;Type;Effect')
for x in range(1, 100):
	#print("Generating card %s" % x)

	card = MinionCard()
	print card.to_csv()