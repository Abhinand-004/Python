import random
import math
names_input = input("Enter customer names (comma-separated): ")
names = [name.strip().title() for name in names_input.split(",") if name.strip()]
unique_names = list(set(names))
random.shuffle(unique_names)
if len(unique_names) < 2:
    print("Not enough participants for a lucky draw (need at least 2).")
else:
    winners = random.sample(unique_names, 2)
    reversed_winners = [winner[::-1] for winner in winners]
    print(" Lucky Draw Results ")
    print(f"Total unique participants: {len(unique_names)}")
    sqrt_participants = round(math.sqrt(len(unique_names)))
    print(f"Square root of participants (rounded): {sqrt_participants}")

    print(f"\nWinner 1: {reversed_winners[0]}")
    print(f"Winner 2: {reversed_winners[1]}")
