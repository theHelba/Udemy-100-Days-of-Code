import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_one_to_five = random.randint(0, 4)

print(friends[random_one_to_five])

print(random.choice(friends))
