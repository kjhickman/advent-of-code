def part1(lines: list[str]) -> int:
    return sum(get_max_joltage(bank, 2) for bank in lines)


def part2(lines: list[str]) -> int:
    return sum(get_max_joltage(bank, 12) for bank in lines)


def get_max_joltage(bank: str, digits: int) -> int:
    result = ""
    space = len(bank) - digits + 1  # the number of chars we can look at
    position = 0

    for i in range(digits):
        max_digit = ""
        max_index = 0
        for j in range(position, space):
            joltage = bank[j]
            if joltage > max_digit:
                max_digit = joltage
                max_index = j

        result += max_digit
        position = max_index + 1
        space = len(bank) - (digits - (i + 1)) + 1

    return int(result)


SAMPLE = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]


def test_part1():
    assert part1(SAMPLE) == 357


def test_part2():
    assert part2(SAMPLE) == 3121910778619
