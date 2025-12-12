def part1(lines: list[str]) -> int:
    grid = [list(line) for line in lines]
    beam_positions = set()
    for row in grid:
        for c, cell in enumerate(row):
            if cell == 'S':
                beam_positions.add(c)

    total_splits = 0
    for row in grid[1:]:
        for x, cell in enumerate(row):
            if cell != '^':
                continue

            if x in beam_positions:
                beam_positions.remove(x)
                total_splits += 1
                if x - 1 >= 0:
                    beam_positions.add(x - 1)
                if x + 1 < len(row):
                    beam_positions.add(x + 1)
    
    return total_splits


def part2(lines: list[str]) -> int:
    total = 0
    return total


SAMPLE = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".strip().splitlines()


def test_part1():
    assert part1(SAMPLE) == 21


def test_part2():
    assert part2(SAMPLE) == 0
