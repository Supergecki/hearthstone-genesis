import generate as gen
import random
import sys

try:
    CARD_NUMBER = int(sys.argv[1])
except (ValueError, IndexError) as e:
    CARD_NUMBER = 10

for x in range(1, CARD_NUMBER + 1):

    card_type = [gen.MinionCard, gen.SpellCard, gen.WeaponCard]
    card = random.choice(card_type)()

    print(card.to_csv() + "\n")
