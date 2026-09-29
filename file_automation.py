import csv
import shutil
from pathlib import Path


# =========================================================
# PYTHON FILE HANDLING & AUTOMATION
# =========================================================
# This program demonstrates:
# 1. Reading a CSV file
# 2. Reading a TXT file
# 3. Writing data into a TXT file
# 4. Renaming a file
# 5. Moving a file
# 6. Deleting a file
# 7. Exception handling using try-except
# =========================================================


# Get the folder where this Python file is located
BASE_FOLDER = Path(__file__).parent

# Define file and folder paths
CSV_FILE = BASE_FOLDER / "students.csv"
TEXT_FILE = BASE_FOLDER / "notes.txt"

ORGANIZED_FOLDER = BASE_FOLDER / "organized_files"
OUTPUT_FOLDER = BASE_FOLDER / "output"

# Create folders automatically if they do not exist
ORGANIZED_FOLDER.mkdir(exist_ok=True)
OUTPUT_FOLDER.mkdir(exist_ok=True)


# =========================================================
# 1. READ CSV FILE
# =========================================================

print("1. Reading CSV file...")

try:
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:

        # DictReader reads CSV data as dictionaries
        reader = csv.DictReader(file)

        students = list(reader)

    print("CSV file read successfully.")
    print("Number of students:", len(students))

except FileNotFoundError:
    print("Error: students.csv file was not found.")

except Exception as error:
    print("Error while reading CSV:", error)


# =========================================================
# 2. READ TEXT FILE
# =========================================================

print("\n2. Reading text file...")

try:
    with open(TEXT_FILE, "r", encoding="utf-8") as file:

        notes = file.read()

    print("Text file read successfully.")
    print("Content:", notes)

except FileNotFoundError:
    print("Error: notes.txt file was not found.")

except Exception as error:
    print("Error while reading text file:", error)


# =========================================================
# 3. WRITE DATA INTO A NEW TEXT FILE
# =========================================================

print("\n3. Creating student report...")

try:
    report_file = OUTPUT_FOLDER / "student_report.txt"

    with open(report_file, "w", encoding="utf-8") as file:

        file.write("STUDENT REPORT\n")
        file.write("=" * 40 + "\n\n")

        for student in students:

            file.write(
                f"Name: {student['Name']}\n"
                f"Course: {student['Course']}\n"
                f"Marks: {student['Marks']}\n"
                f"{'-' * 30}\n"
            )

    print("Student report created successfully.")
    print("Saved at:", report_file)


except Exception as error:
    print("Error while creating report:", error)


# =========================================================
# 4. RENAME THE TEXT FILE
# =========================================================

print("\n4. Renaming text file...")

try:
    renamed_file = BASE_FOLDER / "important_notes.txt"

    # Rename notes.txt to important_notes.txt
    TEXT_FILE.rename(renamed_file)

    # Update the path for further operations
    TEXT_FILE = renamed_file

    print("File renamed successfully.")
    print("New name: important_notes.txt")

except FileNotFoundError:
    print("Error: notes.txt was not found.")

except Exception as error:
    print("Error while renaming file:", error)


# =========================================================
# 5. MOVE THE RENAMED FILE
# =========================================================

print("\n5. Moving file...")

try:
    destination = ORGANIZED_FOLDER / TEXT_FILE.name

    # Move the file to organized_files folder
    shutil.move(str(TEXT_FILE), str(destination))

    print("File moved successfully.")
    print("Moved to:", destination)

except FileNotFoundError:
    print("Error: File to move was not found.")

except Exception as error:
    print("Error while moving file:", error)


# =========================================================
# 6. CREATE A TEMPORARY FILE
# =========================================================

print("\n6. Creating temporary file...")

try:
    temporary_file = BASE_FOLDER / "temporary.txt"

    with open(temporary_file, "w", encoding="utf-8") as file:
        file.write("This is a temporary file.")

    print("Temporary file created successfully.")

except Exception as error:
    print("Error while creating temporary file:", error)


# =========================================================
# 7. DELETE THE TEMPORARY FILE
# =========================================================

print("\n7. Deleting temporary file...")

try:
    temporary_file.unlink()

    print("Temporary file deleted successfully.")

except FileNotFoundError:
    print("Error: Temporary file was not found.")

except Exception as error:
    print("Error while deleting file:", error)


# =========================================================
# PROGRAM COMPLETED
# =========================================================

print("\n" + "=" * 50)
print("FILE HANDLING & AUTOMATION TASK COMPLETED!")
print("=" * 50)