while True:
    print("\nSelect an option:")
    print("1.generate a pattern")
    print("2.analyze a range of numbers")
    print("3.exit")
    
    choice=int(input("enter a choice:"))
     #pattern generater
    if choice==1:
         rows=int(input("enter the number of rows:"))
         for i in range(1,rows+1):
             for j in range(i):
                 print("*",end="")
             print("*")
    elif choice==2:
        start=int(input("enter the starting number:"))
        end=int(input("enter the ending number:"))
        for num in range(start,end+1):
            if num%2==0:
                print("Number",num,"is even")
            else:
                print("Number",num,"is odd")
    elif choice==3:
        print("Existing the program...")
        break
    else:
        print("Invalid choice. Please try again.")