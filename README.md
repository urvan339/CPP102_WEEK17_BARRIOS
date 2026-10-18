# Simulated Device Monitoring and Alert System

**Student Name:** Christian Ross Barrios
**Student Number:** 2601322
**Section:** 1CpE-C

## Project Description

This program monitors simulated device temperature readings. It stores the readings in a list, accepts new valid readings, and classifies each one as NORMAL, WARNING, or CRITICAL. It also prints a numerical summary and an overall monitoring status. It was written for CPP102 Week 17 using only Python 3 built-in features.

## Features

- View all stored temperature readings
- Add a new reading (whole numbers from 0 to 100 only)
- Classify every reading (below 30 is NORMAL, 30 to 35 is WARNING, above 35 is CRITICAL)
- Generate a numerical summary: count, total, average, minimum, maximum, category counts and percentages, and overall status
- Reject invalid menu choices and invalid readings without crashing

## Requirements

- Python 3 (no external packages)

## How to Run

1. Open a terminal inside the Week17 folder.
2. Type: `python device_monitor.py`

## Sample Output

```
MONITORING SUMMARY
------------------
Number of readings  : 6
Total of readings   : 193
Average temperature : 32.17 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL   : 2 (33.33%)
WARNING  : 3 (50.00%)
CRITICAL : 1 (16.67%)

Overall Status: ATTENTION REQUIRED
```

This output was produced after adding the valid reading 33 to the initial list.

## Test Cases

I performed 13 tests (the 10 required tests plus 3 extra). 13 passed and 0 failed. Full details are in [test_cases.md](test_cases.md).

## Known Limitations

- Readings are lost when the program closes, because nothing is saved to a file.
- Readings can only be added, not edited or deleted.
- The 0 to 100 range and the 30 and 35 limits are for this classroom simulation only. They are not real device-safety standards.

## Reflection

In this project I combined lists, loops, selection, and functions into one complete program for the first time. Splitting the work into small functions, with main() controlling the menu loop, made the program easier to understand and test than my earlier single-purpose exercises. The part I found hardest was the input validation order, the boundary tests TC06 and TC07. I tested it with specific values until I understood why it worked. If I continued this project, I would save the readings to a file.