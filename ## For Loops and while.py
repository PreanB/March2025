# For Loops and while
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num + 1)

# For Loops with Range
for i in range(3):
    print(i)

# Nested For Loops
teams = [['Jody', 'Abe'], ['Abhishek', 'Kim'], ['Taylor', 'Jen']]
for team in teams:
    for name in team:
        print(name)

# While Loops
i = 1
while i < 6:
    print(i)
    i += 1

# Example

# for loop
nums = [3, 4, 16]

print('This is an example of for loops')

for num in nums:
    print(num ** 2)

# while loop
i = 3

print('This is an example of while loops')

while i < 258:
    print(i)
    i = i ** 2