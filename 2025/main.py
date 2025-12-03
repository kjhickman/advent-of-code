import importlib
import sys
import time
from pathlib import Path

def get_all_days() -> list[int]:
    """Find all dayXX directories that have a dayXX.py."""
    root = Path(__file__).parent
    days = []
    for d in sorted(root.iterdir()):
        if d.is_dir() and d.name.startswith("day") and (d / f"{d.name}.py").exists():
            try:
                days.append(int(d.name[3:]))
            except ValueError:
                continue
    return days


def run_day(day: int) -> None:
    """Run a single day's solution."""
    day_str = f"day{day:02d}"
    day_dir = Path(__file__).parent / day_str

    if not day_dir.exists():
        print(f"Day {day} not found")
        return

    input_file = day_dir / "input.txt"
    if not input_file.exists():
        print(f"Day {day}: input.txt not found")
        return

    data = input_file.read_text().rstrip().splitlines()

    try:
        module = importlib.import_module(f"{day_str}.{day_str}")
    except ImportError as e:
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
