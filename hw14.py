import random
import math
names_input = input("Enter customer names: ").split(",")
unique_names = list(set(names_input))
winners = random.choices(unique_names, k=2)
reversed_winners = [winner[::-1] for winner in winners]
print(" Lucky Draw Results ")
print(f"Total unique participants: {len(unique_names)}")
sqrt_participants = round(math.sqrt(len(unique_names)))
print(f"Square root of participants: {sqrt_participants}")
print(f"\nWinner 1: {reversed_winners[0]}")
print(f"Winner 2: {reversed_winners[1]}")