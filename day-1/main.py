"""
Dylan Duhamel

--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

"""


# text_line is one line of calibration data. Eg. "a1b2c3d4e5f"
def compute_calibration_value(text_line):
    digit_1 = ""
    digit_2 = ""

    # Check each char from start if number
    for char in text_line:
        if char.isdigit():
            digit_1 = char
            break

    # Check each char from end if number
    for char in reversed(text_line):
        if char.isdigit():
            digit_2 = char
            break

    return int(digit_1 + digit_2)


"""
--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""


# Replace each instance of the numerical word with its associated number.
# Then you can compute calib value with func from pt. 1
def compute_calibration_value_word(text_line):
    digit_words = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for i, digit in enumerate(digit_words):
        if digit in text_line:
            text_line = text_line.replace(digit, digit[0] + str(i + 1) + digit[-1])

    return compute_calibration_value(text_line)


with open("./input.txt", "r") as file:
    text_lines = file.read().splitlines()

sum_1 = 0
sum_2 = 0

for text_line in text_lines:
    sum_1 += compute_calibration_value(text_line)
    sum_2 += compute_calibration_value_word(text_line)

print(f"Solution 1: {sum_1}")
print(f"Solution 2: {sum_2}")
