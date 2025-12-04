import importlib.util
import sys
import time
from pathlib import Path


def get_all_days() -> list[int]:
    """Find all solution files in the solutions directory."""
    solutions_dir = Path(__file__).parent / "solutions"
    days = []
    if solutions_dir.exists():
        for file in sorted(solutions_dir.glob("day*.py")):
            try:
                day = int(file.stem[3:])  # Remove "day" prefix
                days.append(day)
            except ValueError:
                continue
    return days


def run_day(day: int) -> None:
    """Run a single day's solution."""
    day_str = f"day{day:02d}"
    solutions_dir = Path(__file__).parent / "solutions"
    inputs_dir = Path(__file__).parent / "inputs"

    solution_file = solutions_dir / f"{day_str}.py"
    if not solution_file.exists():
        print(f"Day {day} not found")
        return

    input_file = inputs_dir / f"{day_str}.txt"
    if not input_file.exists():
        print(f"Day {day}: input.txt not found")
        return

    data = input_file.read_text().rstrip().splitlines()

    try:
        spec = importlib.util.spec_from_file_location(f"{day_str}", solution_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"Day {day}: Failed to import solution - {e}")
        return

    print(f"--- Day {day:02d} ---")

    for part_num, part_fn in [("1", "part1"), ("2", "part2")]:
        if hasattr(module, part_fn):
            try:
                start = time.perf_counter()
                result = getattr(module, part_fn)(data)
                elapsed = (time.perf_counter() - start) * 1000
                print(f"Part {part_num}: {result} ({elapsed:.2f}ms)")
            except NotImplementedError:
                print(f"Part {part_num}: Not implemented")
            except Exception as e:
                print(f"Part {part_num}: Error - {e}")


def main():
    if len(sys.argv) > 1:
        try:
            day = int(sys.argv[1])
            run_day(day)
        except ValueError:
            print(f"Invalid day: {sys.argv[1]}")
            sys.exit(1)
    else:
        days = get_all_days()
        if not days:
            print("No days found")
        else:
            for day in days:
                run_day(day)
                print()


if __name__ == "__main__":
    main()
