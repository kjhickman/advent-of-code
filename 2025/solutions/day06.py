def part1(lines: list[str]) -> int:
    grid = [line.split() for line in lines]
    total = 0
    for x in range(len(grid[0])):
        # go from bottom to top
        operator = None
        nums = []
        for y in range(len(grid)-1, -1, -1):
            if y == len(grid)-1:
                operator = grid[y][x]
                continue

            nums.append(int(grid[y][x]))

        result = compute_result(nums, operator or '+')
        total += result

    return total


def part2(lines: list[str]) -> int:
    max_col = max(len(line) for line in lines)
    grid = [list(line.ljust(max_col)) for line in lines]
    num_rows = len(grid) - 1  # exclude operator row
    
    empty_cols = []
    for col_idx in range(max_col):
        col = [grid[row][col_idx] for row in range(num_rows)]
        is_empty = all(c == ' ' for c in col)
        if is_empty:
            empty_cols.append(col_idx)
    
    problem_ranges = []
    start = 0
    for empty_col in empty_cols:
        if start < empty_col:
            problem_ranges.append((start, empty_col - 1))
        start = empty_col + 1
    
    # last problem
    if start < max_col:
        problem_ranges.append((start, max_col - 1))
    
    operator_row = grid[-1]
    total = 0
    for start, end in problem_ranges:
        problem_cols_indices = list(range(start, end + 1))
        operator = None
        for col_idx in problem_cols_indices:
            if operator_row[col_idx] in ['+', '*']:
                operator = operator_row[col_idx]
                break
        
        numbers = []
        for col_idx in problem_cols_indices:
            col = [grid[row][col_idx] for row in range(num_rows)]
            num_str = ''.join(c for c in col if c != ' ')
            if num_str:
                numbers.append(int(num_str))
        
        result = compute_result(numbers, operator or '+')
        total += result
    
    return total

def compute_result(numbers: list[int], operator: str) -> int:
    """Compute result based on operator: multiply all or sum all."""
    if operator == '*':
        result = 1
        for n in numbers:
            result *= n
        return result
    else:  # operator == '+'
        return sum(numbers)


SAMPLE = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +
""".strip().splitlines()


def test_part1():
    assert part1(SAMPLE) == 4277556


def test_part2():
    assert part2(SAMPLE) == 3263827
