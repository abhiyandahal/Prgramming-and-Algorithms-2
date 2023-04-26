name = input ("Enter your name:")
percentage = float(input("Enter the percentage: "))

sub1 = int(input("Enter the marks for Maths: "))
sub2 =  int(input("Enter the marks for Science: "))
percentage = ((sub1+sub2)/200)*100

if (sub1 or sub2 < 40):
    print(name, "is fail")
elif percentage >= 70:
    print(name, "is in First Class")
elif percentage >= 60 and percentage < 70:
    print(name, " is in Upper Second Class")
elif percentage >= 50 and percentage < 60:
    print(name, "is in Lower Second Class")
elif percentage >= 40 and percentage < 50:
    print(name, "is in Third Class")
else:
    print(name, "is Fail") 
