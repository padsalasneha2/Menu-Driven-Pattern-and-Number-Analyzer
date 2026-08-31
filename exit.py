def generate_pattern():
    for i in range(2, 6):
        print("*" * i)


def analyze_range():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    total = 0

    for i in range(start, end + 1):

        if i % 2 == 0:
            print("Number", i, "is Even")
        else:
            print("Number", i, "is Odd")

        total = total + i

    print("Sum of all numbers from", start, "to", end, "is:", total)


while True:

    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        generate_pattern()

    elif choice == 2:
        analyze_range()

    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")