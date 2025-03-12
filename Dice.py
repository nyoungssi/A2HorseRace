import random



class Dice:
     def __init__(self, number_side):
         self.Dice = number_side
         self.front_side = None

     def roll(self):
        self.front_side = random.randint(1,6)
        return self.front_side
dice=Dice(6)

result = dice.roll()

print (f"your number is {result}")

