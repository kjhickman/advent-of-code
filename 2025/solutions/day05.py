def part1(lines: list[str]) -> int:
    total = 0
    ranges = []
    break_index = 0
    for i, line in enumerate(lines):
        if line == "":
            break_index = i
            break
        start, end = map(int, line.split("-"))
        ranges.append((start, end))
    
    for id_str in lines[break_index + 1:]:
        id_num = int(id_str)
        for start, end in ranges:
            if start <= id_num <= end:
                total += 1
                break
    return total


def part2(lines: list[str]) -> int:
    ranges = []
    for line in lines:
        if line == "":
            break

        start, end = map(int, line.split("-"))
        ranges.append((start, end))
    
    ranges.sort()
    merged = []
    cur_start, cur_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= cur_end + 1:
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end
    merged.append((cur_start, cur_end))

    total = 0
    for start, end in merged:
        total += end - start + 1
    return total


SAMPLE = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".strip().splitlines()


def test_part1():
    assert part1(SAMPLE) == 3


def test_part2():
    assert part2(SAMPLE) == 14
