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

        new_position = dial_position + num_part

        if num_part >= 0:
            crossings, dial_position = divmod(new_position, 100)
        else:
            last_multiple = (
                dial_position - 100
                if dial_position % 100 == 0
                else (dial_position // 100) * 100
            )
            first_multiple = ((new_position - 1) // 100 + 1) * 100
            crossings = max(0, (last_multiple - first_multiple) // 100 + 1)
            dial_position = new_position % 100

        password += crossings

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

EDGECASE = [
    "L49",
    "L101",
]


def test_part1():
    assert part1(SAMPLE) == 3


def test_part2():
    assert part2(SAMPLE) == 6


def test_part2_edgecase():
    assert part2(EDGECASE) == 2
