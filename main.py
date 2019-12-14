import generate as gen
import random

CARD_NUMBER = 10

for x in range(1, CARD_NUMBER + 1):

    card_type = [gen.MinionCard, gen.SpellCard, gen.WeaponCard]
    card = random.choice(card_type)()

    print(card.to_csv() + "\n")
