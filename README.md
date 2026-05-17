# Student Grade Tracker

A Python practice project focused on **list/dict comprehensions**. Stores students with randomly generated grades and provides GPA-based analysis functions.

## What I Practiced
- List comprehensions with conditions
- Dict comprehensions
- Helper functions with single responsibility
- JSON read/write with merge logic

## Functions

| Function | Description |
|---|---|
| `add_student()` | Adds a student with random grades and current year |
| `calculate_gpa(name)` | Converts grades to GPA points and averages them |
| `filter_by_range(min, max)` | Returns students within a GPA range |
| `sort_by_gpa(reverse)` | Sorts all students by GPA ascending or descending |
| `get_top_n(n)` | Returns top N students by GPA |
| `export_to_json()` | Exports data to `students.json`, preserving existing entries |

## GPA Scale

| Percentage | Points |
|---|---|
| 90–100 | 4.0 |
| 80–89 | 3.0 |
| 70–79 | 2.0 |
| 60–69 | 1.0 |
| Below 60 | 0.0 |

## Run

```bash
python student_tracker.py
```

## Note
Grades are generated with `random.randint()` — the focus of this project is the comprehension logic, not data input.
