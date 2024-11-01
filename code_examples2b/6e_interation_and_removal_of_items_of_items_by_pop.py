guests = ['Albert Einstein', 'Linus Pauling', 'Marie Curie', 'Rosalind Franklin', 'Walt Disney',
          'Mary Anning']


print("Before...")
print(guests)
print()

for _ in range(len(guests), 2, -1):
    dismissed_guest = guests.pop()
    print(f"{dismissed_guest} is uninvited to the dinner party")

print("\nAfter...")
print(guests)
