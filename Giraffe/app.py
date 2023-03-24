from math import *


def say_hi(name):
    print("Hello " + name)


def cube(num):
    return num*num*num


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter

    return translation


print("Hello world")
print("   /|")
print("  / |")
print(" /  |")

print("/___|")

character_name = "Michael"
character_age = 35
is_male = True

print("There once was a man named " + character_name + ".")
print("Giraffe Academy")

phrase = "Giraffe Academy"
print(phrase + " is cool.")
print(phrase.lower())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase[7])
print(phrase.index("ffe"))
print(phrase.replace("Giraffe", "Elephant"))
print(-2.554)
print(2/3)

my_num = 654
my_num_string = str(my_num)
print(my_num_string + " is a number")

print(floor(5.6))
print(ceil(5.7))
print(sqrt(39))

friends = ["Kevin", "Karen", "Jim"]
numbers = [4, 5, 6]
print(friends)
print(friends[0])
friends.extend(numbers)
print(friends)

say_hi("Mike")

print(cube(4))

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are not a male and not tall")

print(max_num(300, 40, 5))

for letter in "Giraffe Academy":
    print(letter)

print(2**3)
print(raise_to_power(4, 5))

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[1][0])

for row in number_grid:
    for col in row:
        print(col)

number = input("Enter a number: ")
digits = {
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine",
    '0': "zero",
}

output = ""
for x in number:
    output += digits.get(x, "!") + " "

print(output)
