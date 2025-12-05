def part1(lines: list[str]) -> int:
    total = 0
    grid = to_grid(lines)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if is_accessible(grid, x, y, 3):
                total += 1
    return total


def part2(lines: list[str]) -> int:
    total = 0
    grid = to_grid(lines)
    while True:
        to_remove = []
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if is_accessible(grid, x, y, 3):
                    to_remove.append((x, y))
                    total += 1
        if len(to_remove) == 0:
            break
        for x, y in to_remove:
            grid[y][x] = "."
    return total


def is_accessible(grid: list[list[str]], x: int, y: int, max_adjacent: int) -> bool:
    if grid[y][x] != "@":
        return False

    directions = [(-1, -1), (0, -1), (1, -1),
                  (-1,  0),          (1,  0),
                  (-1,  1), (0,  1), (1,  1)]

    total_adjacent = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if grid[ny][nx] == "@":
                total_adjacent += 1
    return total_adjacent <= max_adjacent


def to_grid(lines: list[str]) -> list[list[str]]:
    return [list(line) for line in lines]


SAMPLE = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".strip().splitlines()


def test_part1():
    assert part1(SAMPLE) == 13


def test_part2():
    assert part2(SAMPLE) == 43
