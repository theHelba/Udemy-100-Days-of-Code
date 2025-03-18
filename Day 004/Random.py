import random

randomInt = random.randint(1, 10)
print(randomInt)

# Default is 0 - 0.9999999999
randomFloatOneToTen = random.random() * 10
print(randomFloatOneToTen)

randomFloat = random.uniform(25, 50)
print(randomFloat)

headsOrTails = random.randint(1, 10)
if headsOrTails % 2 == 0:
    print("Heads!")
elif headsOrTails % 2 != 0:
    print("Tails!")
