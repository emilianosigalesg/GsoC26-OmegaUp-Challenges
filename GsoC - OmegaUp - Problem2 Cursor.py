import sys


GRADE_ORDER = "ABCDEF"
GRADE_INDEX = {grade: idx for idx, grade in enumerate(GRADE_ORDER)}


def count_course_grades(grades_line: str, expected_count: int) -> list[int]:
    """Count A-F occurrences from a course grades line."""
    counts = [0] * len(GRADE_ORDER)

    # Split handles repeated spaces cleanly.
    grades = grades_line.split()
    if expected_count > 0:
        grades = grades[:expected_count]

    for grade in grades:
        if grade in GRADE_INDEX:
            counts[GRADE_INDEX[grade]] += 1
    return counts


def format_counts(prefix: str, counts: list[int]) -> str:
    return (
        f"{prefix}A:{counts[0]} B:{counts[1]} C:{counts[2]} "
        f"D:{counts[3]} E:{counts[4]} F:{counts[5]}"
    )


def main() -> None:
    data = sys.stdin
    t = int(data.readline().strip())

    all_courses = []
    total = [0] * len(GRADE_ORDER)

    for _ in range(t):
        s = int(data.readline().strip())
        grades_line = data.readline().strip()

        counts = count_course_grades(grades_line, s)
        all_courses.append(counts)

        for i in range(len(GRADE_ORDER)):
            total[i] += counts[i]

    output_lines = [format_counts("", counts) for counts in all_courses]
    output_lines.append(format_counts("TOTAL: ", total))
    print("\n".join(output_lines))


if __name__ == "__main__":
    main()
