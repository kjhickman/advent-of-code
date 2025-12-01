def part1(lines: list[str]) -> int:
    dial_position: int = 50
    password: int = 0
    for line in lines:
        char_part = line[0]
        num_part = int(line[1:])
        if char_part == "L":
            num_part = -num_part
        new_position = (dial_position + num_part) % 100
        if new_position < 0:
            new_position += 100
        if new_position == 0:
            password += 1
        dial_position = new_position
        
    return password

def part2(lines: list[str]) -> int:
    dial_position: int = 50
    password: int = 0
    for line in lines:
        char_part = line[0]
        num_part = int(line[1:])
        if char_part == "L":
            num_part = -num_part
        quotient, new_position = divmod(dial_position + num_part, 100)
        if new_position < 0:
            new_position += 100
        password += abs(quotient)
        dial_position = new_position
        
    return password

SAMPLE = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]

def test_part1():
    assert part1(SAMPLE) == 3

def test_part2():
    assert part2(SAMPLE) == 6

