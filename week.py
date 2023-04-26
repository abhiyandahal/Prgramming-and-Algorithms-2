day = int(input("Enter a number: "))

match day:
    case 1:
        print("Today is Sunday.")
    case 2:
        print("Today is Monday.")
    case 3:
        print("Today is Tuesday.")    
    case 4:
        print("Today is Wednesday.")
    case 5:
        print("Today is Thursday.")
    case 6:
        print("Today is Friday.")
    case 7:
        print("Today is Saturday.") 
    case _:
        print("PLease enter value in between 1-7.")
