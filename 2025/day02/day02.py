def part1(lines: list[str]) -> int:
    total = 0
    ranges = lines[0].split(",")
    for r in ranges:
        start, end = map(int, r.split("-"))
        for num in range(start, end + 1):
            if not is_valid(str(num), 2):
                total += num
    return total

def part2(lines: list[str]) -> int:
    total = 0
    ranges = lines[0].split(",")
    for r in ranges:
        start, end = map(int, r.split("-"))
        for num in range(start, end + 1):
            num_str = str(num)
            for seq_length in range(2, len(num_str) + 1):
                if not is_valid(num_str, seq_length):
                    total += num
                    break
    return total

def is_valid(num: str, seq_length: int) -> bool:
    length = len(num)
    if length % seq_length != 0:
        return True
    part = length // seq_length
    pattern = num[:part]
    should_be = pattern * seq_length
    result = num != should_be
    return result


SAMPLE = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def test_part1():
    assert part1([SAMPLE]) == 1227775554

def test_part2():
    assert part2([SAMPLE]) == 4174379265
