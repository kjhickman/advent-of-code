import importlib.util
import sys
import time
from pathlib import Path


def get_all_days() -> list[int]:
    solutions_dir = Path(__file__).parent / "solutions"
    return [int(f.stem[3:]) for f in sorted(solutions_dir.glob("day*.py"))]


def run_day(day: int) -> None:
    day_str = f"day{day:02d}"
    solutions_dir = Path(__file__).parent / "solutions"
    inputs_dir = Path(__file__).parent / "inputs"
    solution_file = solutions_dir / f"{day_str}.py"
    input_file = inputs_dir / f"{day_str}.txt"
    data = input_file.read_text().rstrip().splitlines()
    spec = importlib.util.spec_from_file_location(day_str, solution_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    print(f"--- Day {day:02d} ---")
    for part_num, part_fn in [("1", "part1"), ("2", "part2")]:
        fn = getattr(module, part_fn, None)
        if fn:
            start = time.perf_counter()
            result = fn(data)
            elapsed = (time.perf_counter() - start) * 1000
            print(f"Part {part_num}: {result} ({elapsed:.2f}ms)")


def main():
    if len(sys.argv) > 1:
        run_day(int(sys.argv[1]))
    else:
        for day in get_all_days():
            run_day(day)
            print()


if __name__ == "__main__":
    main()
