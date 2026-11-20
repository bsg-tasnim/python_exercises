
import pandas as pd
col_name = ["Name","Age","Grade","Mark"]
def validate_csv(filename):
    total_pass = 0
    total_fail = 0
    df = pd.read_csv(filename)

    if list(df.columns)!=col_name:
        print("Invalid column names")
        return
    for num, row in df.iterrows():
        errors = []
        if pd.notna(row["Name"]):
            name= str(row["Name"]).strip()
        else:
            name = ""

        age = row["Age"]
        grade = str(row["Grade"]).strip()
        mark = row["Mark"]

        if not name:
            errors.append("Name cannot be empty")

        if pd.isna(age) or not float(age).is_integer():
            errors.append("Age must be a valid integer")
        elif not (0 <= int(age) <= 100):
            errors.append("Age must be between 0 and 100")

        if grade.upper() not in ["A","B","C","D","F"]:
            errors.append("Invalid grade")

    
        if pd.isna(mark):
            errors.append("Mark must be a number")
        else:
            try:
                mark = float(mark)
                if not (0 <= mark <= 100):
                    errors.append("Mark must be between 0 and 100")
            except ValueError:
                errors.append("Mark must be a number")

        if errors:
            total_fail += 1
            print(f"Row {num+2}: Failed - {','.join(errors)}")
        else:
            total_pass += 1
            print(f"Row {num + 2}: Passed")
    print(f"Total Passed:{total_pass}")
    print(f"Total Failed:{total_fail}")



csv_file = "/home/blockstak/Documents/program/test_data.csv"
validate_csv(csv_file)
