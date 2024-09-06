Mark = int(input("Enter the obtained mark: "))

if Mark>=101:
    print("please verify your grade again ")
    exit()

if Mark >=90:
    grade="A"
elif Mark>=80:
    grade="B"
elif Mark>=60:
    grade="c"
elif Mark>=50:
    grade="D"
else:
    grade="F"
print("Grade: ", grade)