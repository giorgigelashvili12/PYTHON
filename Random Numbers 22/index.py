import random 
# have access to anything random
x = random.randint(1, 6)
# random number on a scale of 1 to 6
y = random.random()
# random number, like 0.78787817283728378

myList = ['rock', 'paper', 'scissorts']
z = random.choice(myList)
# generates random choice from a list

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards)
# stores elements on random indexes