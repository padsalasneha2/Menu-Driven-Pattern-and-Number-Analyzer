start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

total = 0

for i in range(start, end + 1):
    
    if i % 2 == 0:
        print("Number", i, "is Even")
    else:
        print("Number", i, "is Odd")
    
    total = total + i

print("Sum of numbers from", start, "to", end, "is:", total)