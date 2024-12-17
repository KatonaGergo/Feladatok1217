import random

random_numbers = []
greater_than_zero_numbers = 0
lower_than_zero_numbers = 0


for number in range(100):
    random_number = random.randint(-100, 100)
    random_numbers.append(random_number)
    

for szam in random_numbers:
    if szam > 0:
        greater_than_zero_numbers += 1
    elif szam < 0:
        lower_than_zero_numbers += 1
        
if greater_than_zero_numbers > lower_than_zero_numbers:
    print("A 0-tól nagyobb számokból van több.")
else:
    print("A 0-tól kisebb számokból van több.")    

found = False
for index, number in enumerate(random_numbers):
    if number > 50:
        print(f"Az első 50-nél nagyobb szám: {number} sorszáma: {index}")
    found = True
    
if not found:
    print("Nincs 50-től nagyobb szám!")
    
for i in range(len(random_numbers) - 1):
    if abs(random_numbers[i] - random_numbers[i + 1]) > 120:
        print(f"Van olyan eset, hogy két egymást követő szám különbsége meghaladja a 120-at: ({random_numbers[i]}, {random_numbers[i + 1]})")
else:
    print("Nincs olyan eset, hogy két egymást követő szám különbsége meghaladja a 120-at.")