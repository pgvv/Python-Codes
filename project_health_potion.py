import random

health = 50  # Default Health Level

"""
Difficulty mode:
1: Easy
2: Medium
3: Difficult
"""
difficulty =1  # Difficulty Level

potion_health = int(random.randint(25,50) / difficulty)

health += potion_health

print(health)
