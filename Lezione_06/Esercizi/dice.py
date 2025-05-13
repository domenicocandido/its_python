import random
class Dice:

    def __init__(self, sides:int = 6) -> None:
        
        self.sides = sides

    def roll_dice(self) -> None:

        return random.randint(1, self.sides)

dado6:Dice = Dice()
total_rolls = []
for roll in range(10):

    rolls = dado6.roll_dice()
    total_rolls.append(rolls)

print(f"Tirando il dado di 6 facce per 10 volte otteniamo le facce:\n{total_rolls}")

dado10:Dice = Dice(sides = 10)
total_rolls =  []

for roll in range(10):

    rolls = dado10.roll_dice()
    total_rolls.append(rolls)

print(f"\nTirando il dado di 10 facce per 10 volte otteniamo le facce:\n{total_rolls}")

dado20:Dice = Dice(sides = 20)
total_rolls =  []

for roll in range(10):

    rolls = dado20.roll_dice()
    total_rolls.append(rolls)

print(f"\nTirando il dado di 20 facce per 10 volte otteniamo le facce:\n{total_rolls}")

