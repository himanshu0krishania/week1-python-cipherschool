a, b, c = input("Enter DD/MM/YYYY and then press Enter: ").split("/")
print("to")
A, B, C, = input("Enter DD/MM/YYYY: ").split("/")
Year = int(c)
toYear = int(C)
Date = int(a)
toDate = int(A)
Month = int(b)
toMonth = int(B)

if Date and toDate<=31 and(Date and toDate)>0:
    if Month and toMonth<=12 and(Month and toMonth)>0:
        if Year and toYear>=1000 and (Year != toYear) and (toYear>Year):
            print("There are non leap Years in this Range listed below:")
            for i in range(Year, toYear + 1):
                if i % 4 > 0 or (i%100 ==0 and i % 400 !=0 ):
                    print(i, end=" ")
                    continue
            print("\nThere are leap year in this Range listed below:")
            for z in range(Year, toYear + 1 ):
                if z%400==0 or z%100!=0 and z%4==0:
                    print(z,end=" ")
        else:
            print("Input Correct Year.")
    else:
        print("Input Correct Month.")
else:
    print("Input Correct Date.")


