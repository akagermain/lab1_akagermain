# Lab 1: Grade Evaluator & Archiver

## What's in this repository
- `grade-evaluator.py` — reads a grades CSV file (filename entered by you at the prompt. In this case, grades.csv which was provided was the one to be used), validates it, calculates the GPA, decides PASSED/FAILED, and shows which Formative assignment(s) qualify for resubmission.
- `organizer.sh` — archives `grades.csv` with a timestamp, resets the workspace, and logs the action.
- `Readme.md` — this file.

## Requirements
- Python 3
- Bash (Linux/macOS terminal, or Ubuntu terminal / WSL on Windows) 

## 1. How to run `grade-evaluator.py`

1. Make sure your CSV file is in the same folder as `grade-evaluator.py`.
2. The CSV must have this header and format:

   ```
   assignment,group,score,weight
   Quiz,Formative,85,20
   Midterm Project,Summative,70,20
   ```

   - `group` must be `Formative` or `Summative`
   - `weight` values must add up to 100 overall (60 for Formative, 40 for Summative)
   - `score` must be between 0 and 100

3. Run the script:

   ```bash
   python3 grade-evaluator.py
   ```

4. When prompted, type the filename, e.g.:

   ```
   Enter the name of the CSV file to process (e.g., grades.csv): grades.csv
   ```

5. The script prints a report: total grade, category percentages, final GPA, PASSED/FAILED status, and any Formative assignment(s) eligible for resubmission.

If the file is missing, empty, contains an out-of-range score, or the weights don't add up correctly, the script prints a clear error message and stops instead of crashing.

## 2. How to run `organizer.sh`

1. Make sure `organizer.sh` is in the same folder as `grades.csv`.
2. Give it permission to run (only needed once):

   ```bash
   chmod +x organizer.sh
   ```

3. Run it:

   ```bash
   ./organizer.sh
   ```

4. What happens each time you run it:
   - Creates an `archive/` folder if it doesn't already exist
   - Renames the current `grades.csv` with a timestamp (e.g. `grades_20260722-140224.csv`) and moves it into `archive/`
   - Creates a brand-new, empty `grades.csv` in the current folder
   - Adds a line to `organizer.log` recording the timestamp, the original filename, and the new archived filename

You can run it as many times as you want — every run adds a new entry to `organizer.log` without deleting previous ones.
