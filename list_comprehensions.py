"""
CP1404/CP5632 - Practical 4
List comprehensions
"""
names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]
almost_numbers = ['0', '10', '21', '3', '-5', '89', '121']

a_names = [name for name in full_names if name.startswith('A')]
print(a_names)

initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(initials)

lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

numbers = [int(number_str) for number_str in almost_numbers]
print(numbers)

large_numbers = [number for number in numbers if number > 9]
print(large_numbers)

last_names_string = " ".join([name.split()[1] for name in full_names])
print(last_names_string)