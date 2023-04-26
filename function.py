a=int(input('Enter First Number: '))

b=int(input('Enter Second Number: '))

while True:

    print('   1.Addition\n   2.Subtraction\n   3.Multiplication\n   4.Division\n   5.Exit')

    print('-------------------------------------------------------------------')

    ch=int(input('Enter your choice from 1 to 4 for Arithmetic Opeations: '))   

    if ch==1:

            print("The sum of two number  is ",a+b)   

    elif ch==2:

            print('The subtraction of two number is ',a-b)

    elif ch==3:

            print('The Multiplication of two number is ',a*b)      

    elif ch==4:

            print('The Division of two number is ',a/b)

    elif ch==5:

            break

    else:

        print('Please enter the value from 1 to 4')

    ans=input('Do you want to Continue Again(Y/N)')

    if ans.upper()=='Y':

        continue

    else:

        break

