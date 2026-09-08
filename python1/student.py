students = []
while True:
    print("-------student mangament------")
    print("1.add student")
    print("2.view students")
    print("3.exit")
    choice = int(input("enter your choice: "))
    if choice == 1:
        name = input("enter student name: ")
        age = int(input("enter student age: "))
        course = input("enter student course: ")
        students.append({"name": name, "age": age, "course": course})
    elif choice == 2:
        print("-------students-------")
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")
    elif choice == 3:
        print("Existing the program...")
        break
    else:
        print("Invalid choice. Please try again.")