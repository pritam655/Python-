students = {}

while True:
    print("1 Add 2 View 3 Delete 4 Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        sid = input("ID: ")
        name = input("Name: ")
        students[sid] = name

    elif ch == 2:
        print(students)

    elif ch == 3:
        sid = input("Enter ID to delete: ")
        students.pop(sid, None)

    else:
        break