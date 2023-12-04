"""
Dylan Duhamel

Day 1 - Trebuchet
"""


def part_one(input):
    calibrationValue = 0
    digit1, digit2 = None, None

    for char in input:
        if char == "\n" and digit1 is not None and digit2 is not None:
            calibrationValue += int(digit1 + digit2)
            digit1, digit2 = None, None
        elif char == "\n" and digit1 is not None and digit2 is None:
            calibrationValue += int(digit1 + digit1)
            digit1 = None
        elif digit1 is None and char.isdigit():
            digit1 = char
        elif char.isdigit():
            digit2 = char

    if digit1 is not None and digit2 is not None:
        calibrationValue += int(digit1 + digit2)
    elif digit1 is not None and digit2 is None:
        calibrationValue += int(digit1 + digit1)

    return calibrationValue


def checkDigit(string, idx):
    digitText = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digitToCheck = ""

    for i in range(idx, len(string)):
        digitToCheck += string[i]

        if digitToCheck in digitText:
            return digitToCheck

    return None


def part_two(input):
    calibrationValue = 0
    digit1, digit2 = None, None
    inputLines = input.split("\n")
    digitText = ["o", "t", "f", "s", "e", "n"]

    for line in inputLines:
        for i, char in enumerate(line):
            if char == "\n" and digit1 is not None and digit2 is not None:
                calibrationValue += int(digit1 + digit2)
                digit1, digit2 = None, None
            elif char == "\n" and digit1 is not None and digit2 is None:
                calibrationValue += int(digit1 + digit1)
                digit1 = None
            elif digit1 is None and char.isdigit():
                digit1 = char
            elif char.isdigit():
                digit2 = char
            elif char in digitText:
                temp = checkDigit(line, i)
                if digit1 is None and temp:
                    digit1 = temp
                elif temp:
                    digit2 = temp

    print(digit1)
    print(digit2)
    print(int(digit1 + digit2))
    return calibrationValue


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        inputText = file.read()

    print(part_two(inputText))
