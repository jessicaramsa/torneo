import random

people = []

directPass = random.choice(people)
print(f'Direct pass: {directPass}')
uroboros.remove(directPass)

random.shuffle(people)
print(people)
