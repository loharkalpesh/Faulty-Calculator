# 45 * 3 = 555 , 56+9=77 , 56/6=4
# Faulty Calculater

while True:
    a=int(input("Enter number #1:"))
    b=int(input("Enter number #2:"))

    print("\nEnter + for Addition")
    print("Enter - for Subtraction")
    print("Enter * for Multiplication")
    print("Enter / for Divition\n")

    query=input("What you do?:")
    print()

    if a==45:
        if b==3:
            if query=="+":
                print("Your Answer is 555.")

    if a==56:
        if b==9:
            if query=="+":
                print("Your Answer is 77.")
        elif b==6:
            if query=="/":
                print("Your Answer is 4.")

    if a!=45 or b!=3:
        if a!=56 or b != 9:
            if b !=6:
                if query=="+":
                    print("Your Answer is",a+b)
                elif query=="-":
                    print("Your Answer is",a-b)
                elif query=="*":
                    print("Your Answer is",a*b)
                elif query=="/":
                    if b==0:
                        print("Division is not Possible.")
                    else:
                        print("Your Answer is",a/b)
    res=int(input("\nDo You Want To do again press 1(means yes) or 0(means no): "))
    if res == 0:
        break
        exit
input("Press Enter")
