import random

derivative_is_higher_than_zero_count = 0
derivative_is_higher_than_zero_count_backwards = 0
random_numbers = []

for iteration in range(30):
    random_number = random.randint(0, 9)
    random_numbers.append(random_number)


for i in range(1, len(random_numbers) - 1):
    if random_numbers[i] >= random_numbers[i-1] + 2:
        print(f"Az útszakasz {i}. helyen meredek.")
        derivative_is_higher_than_zero_count += 1

print(f"Az úton {derivative_is_higher_than_zero_count} meredek szakasz volt.")

for i in range(len(random_numbers)-2, 0, -1):
    if random_numbers[i] >= random_numbers[i+1] + 2:
        print(f"Az útszakasz visszafelé {i}. helyen meredek.")
        derivative_is_higher_than_zero_count_backwards += 1

print(f"Az útszakasz visszafelé vezető útján {derivative_is_higher_than_zero_count_backwards} meredek szakasz volt.")