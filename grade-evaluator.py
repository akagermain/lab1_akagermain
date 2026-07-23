import csv
import sys
import os

def load_csv_data():
    # The user is prompted for a filename, checks if it exists, and extract all fields into a list of dictionaries.
    filename = input('Enter the name of the CSV file to process (e.g, grades.csv): ')

    if not os.path.exists(filename):
        print(f'Error: The file "{filename}" was not found.')
        sys.exit(1)

    assignment = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for now in reader:
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

