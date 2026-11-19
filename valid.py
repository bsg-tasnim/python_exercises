import csv
col_name = ["Name", "Age", "Grade", "Mark"]

def validate_csv(filename):
    
    total_pass = 0
    total_fail = 0

    with open(filename, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames != col_name:
            print("Invalid column names")
            return
        
        for num, row in enumerate(reader, start=2):
            errors = []
            name = (row.get("Name") or "").strip()
            age = (row.get("Age") or "").strip()
            grade = (row.get("Grade") or "").strip()
            mark = (row.get("Mark") or "").strip()

            if not name:
                errors.append(f"Name cannot be empty")
      
            if not age.isdigit():
                errors.append(f"Age must be a number")
            elif not (0<= int(age)<= 100):
                errors.append(f"Age must be between 0 and 100")

            if grade.upper() not in ["A", "B", "C", "D", "F"]:
                errors.append(f"Invalid grade")

            try:
                mark_value = float(mark)
                if not (0 <= mark_value <= 100):
                    errors.append(f"Mark must be between 0 and 100")
            except ValueError:
                errors.append(f"Mark must be a number")

            if errors:
                total_fail += 1
                print(f"Row {num}: Fail - {', '.join(errors)}")
            else:
                total_pass += 1
                print(f"Row {num}: Pass")

    print(f"Total Passed: {total_pass}")
    print(f"Total Failed: {total_fail}")
csv_file = "/home/blockstak/Documents/program/test_data.csv"
validation_errors = validate_csv(csv_file)

