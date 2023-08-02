import csv


def print_employees(employees):
    print("Id,ManagerId,LastName,FirstName")
    for employee in employees:
        print(
            f"{employee['id']},{employee['manager_id']},{employee['last_name']},{employee['first_name']}"
        )


def main():
    rows = {}
    with open("employees.csv", "r") as file:
        # "hardwiring" the file name is bad style!
        reader = csv.DictReader(file)
        # next(reader)
        current_id = 1
        for row in reader:
            rows[f"{row['FirstName']} {row['LastName']}"] = {
                "id": str(current_id),
                "manager": row["Manager"],
                "last_name": row["LastName"],
                "first_name": row["FirstName"],
            }
            current_id += 1
    for row in rows.values():
        manager_id = ""
        if row["manager"] != "":
            manager_id = str(rows[row["manager"]]["id"])
        row["manager_id"] = manager_id
        del row["manager"]
    rows = list(rows.values())
    print_employees(rows)


if __name__ == "__main__":
    main()
