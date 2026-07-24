import csv
import sys
import os

def load_csv_data():
    # The user is prompted for a filename, checks if it exists, and extract all fields into a list of dictionaries.
    filename = input('Enter the name of the CSV file to process (e.g, grades.csv): ')

    if not os.path.exists(filename):
        print(f'Error: The file "{filename}" was not found.')
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Converts numeric fields into floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occured while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    print("\n=== Processing Grades ===")
    if not data:
        print("Error: No assignment data found. The CSV file is empty.")
        sys.exit(1)
   # Checking if every score recorded has a valid percentage (0-100)
    for record in data:
        if record['score'] < 0 or record['score'] > 100:
            print(f"Error: '{record['assignment']}' has an invalid score of "
                  f"{record['score']}. Scores must be between 0 and 100."
                  )
            sys.exit(1)
        if record['group'] not in ('Formative', 'Summative'):
            print(f"Error: '{record['assignment']}' has an unkown group"
                  f"'{record['group']}'. Must be 'Formative' or 'Summative'.")
            sys.exit(1)

   # Validating total weights (i.e total has to be 100, summative 40, and Formative 60)
    total_weight = sum(r['weight'] for r in data)
    formative_weight = sum(r['weight'] for r in data if r['group'] == 'Formative')
    summative_weight = sum(r['weight'] for r in data if r['group'] == 'Summative')

    if round(total_weight, 2) != 100:
        print(f"Error: total weight is {total_weight}, but it must equal exactly 100.")
        sys.exit(1)
    if round(formative_weight, 2) != 60:
        print(f"Error: Formative weight is {formative_weight}, but it must equal exactly 60.")
        sys.exit(1)
    if round(summative_weight, 2) != 40:
        print(f"Error: Summative weight is {summative_weight}, but it must equal exactly 40.")
        sys.exit(1)
   # Calculating the final Grade and GPA
    formative_earned = sum((r['weight'] * r['score']) / 100 for r in data if r['group'] == 'Formative')
    summative_earned = sum((r['weight'] * r['score']) / 100 for r in data if r['group'] == 'Summative')
    total_grade = formative_earned + summative_earned
    gpa = (total_grade / 100) * 5.0

    formative_pct = (formative_earned / formative_weight) * 100 if formative_weight else 0
    summative_pct = (summative_earned / summative_weight) * 100 if summative_weight else 0

   # Determining pass and fail status
    status = "PASSED" if formative_pct >= 50 and summative_pct >= 50 else "FAILED"

   # Finding failed formative assignments and keeping only the ones with the highest score
    failed_formatives = [r for r in data if r['group'] == 'Formative' and r['score'] < 50]
    resub_candidates = []
    if failed_formatives:
        highest_weight = failed_formatives[0]['weight']
        for r in failed_formatives:
            if r['weight'] > highest_weight:
                highest_weight = r['weight']
        resub_candidates = [r for r in failed_formatives if r['weight'] == highest_weight]

   # The final decision and resubmission options
    print("=" * 55)
    print("GRADE EVALUATION REPORT")
    print("=" * 55)
    print(f"Total Weighted Grade : {total_grade:.2f} / 100")
    print(f"Summative Score      : {summative_pct:.2f}%  (category weight: {summative_weight:.0f})")
    print(f"Formative Score      : {formative_pct:.2f}%  (category weight: {formative_weight:.0f})")
    print(f"Final GPA            : {gpa:.2f} / 5.0")
    print(f"Final Status         : {status}")
    print("-" * 55)

    if resub_candidates:
        print("Resubmission Eligible (highest-weight failed Formative assignment(s)):")
        for r in resub_candidates:
            print(f"  - {r['assignment']}  (Weight: {r['weight']:.0f}, Score: {r['score']:.0f})")
    else:
        print("No Formative assignment failed. No resubmission needed.")

    print("=" * 55)

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)
