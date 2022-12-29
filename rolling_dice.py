from random import randint
import pygal

class Dice():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    
    def roll(self):
        return randint(1, self.num_sides)

dice_1 = Dice()
dice_2 = Dice()

def roll_one_dice():
    results = []
    for roll_num in range(100):
        result = dice_1.roll()
        results.append(result)

    frequencies = []
    for value in range(1, dice_1.num_sides + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # Histogram
    hist = pygal.Bar()
    hist.title = "Results of rolling two dice 1000 times"
    hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_title = 'Result'
    hist.y_title = 'Frequency of Result'

    hist.add('D6', frequencies)
    hist.render_to_file('dice_visual.svg')

def roll_two_dices():
    results = []
    for roll_num in range(100):
        result = dice_1.roll() + dice_2.roll()
        results.append(result)

    frequencies = []
    max_result = dice_1.num_sides + dice_2.num_sides
    for value in range(2, max_result + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # Histogram
    hist = pygal.Bar()
    hist.title = "Results of rolling two dice 1000 times"
    hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    hist.x_title = 'Result'
    hist.y_title = 'Frequency of Result'

    hist.add('D6 + D6', frequencies)
    hist.render_to_file('two_dice_visual.svg')

msg = int(input("How many dices do you want to roll? (1/2): "))

if msg == 1:
    roll_one_dice()
else:
    roll_two_dices()