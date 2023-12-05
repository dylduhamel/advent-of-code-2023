import re

"""
--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

"""


def find_numbers_with_match(
    prev_line: str | None, line: str, next_line: str | None) -> list[int]:
    numbers = []
    # Returns an iterator over all matches (0-9) in the line
    for number in re.finditer("[0-9]+", line):
        # Tuple of starting and ending index of the matched string
        first_idx, last_idx = number.span()
        last_idx -= 1  # Idx of last number, not idx before

        left_idx = first_idx - 1 if first_idx - 1 >= 0 else first_idx
        right_idx = last_idx + 1 if last_idx + 1 < len(line) else last_idx

        symbol_left = symbol_right = symbol_top = symbol_bottom = False

        symbol_left = first_idx - 1 >= 0 and line[first_idx - 1] != "."
        symbol_right = last_idx + 1 < len(line) and line[last_idx + 1] != "."

        # Check the rows above and below for special character
        # The width is one wide on left and right of the number (this is how we check diagonals ;))
        if prev_line is not None:
            # Will be True if re matches with any symbol
            sub_string = prev_line[left_idx : right_idx + 1]
            symbol_top = re.match("^[0-9.]+$", sub_string) is None
        if next_line is not None:
            sub_string = next_line[left_idx : right_idx + 1]
            symbol_bottom = re.match("^[0-9.]+$", sub_string) is None

        if symbol_left or symbol_right or symbol_top or symbol_bottom:
            numbers.append(int(number.group()))
    
    return numbers

def compute_valid_part_numbers(lines):
    sum_1 = 0

    for line_idx, line in enumerate(lines):
        prev_line = lines[line_idx - 1] if line_idx - 1 >= 0 else None
        next_line = lines[line_idx + 1] if line_idx + 1 < len(lines) else None
        numbers = find_numbers_with_match(prev_line, line, next_line)

        for num in numbers:
            sum_1 += num

    return sum_1


with open("./input.txt", "r") as file:
    lines = [x.strip() for x in file.readlines()]

print(f"Solution 1: {compute_valid_part_numbers(lines)}")
