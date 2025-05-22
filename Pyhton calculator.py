print("Hey there, welcome to the Python calculator!")
a = int(input("Enter first number here:"))
b = int(input("Enter second number here:")) 
calculation = str(input("Finally, type the calculation you want to make:"))
subtraction = a - b or b - a
addition = a + b
multiplication = a * b
division = a/b or b/a 
if calculation == str("addition"):
    sum = a + b 
    print("This is your sum:", sum)
else:
     if calculation == str("subtraction"):
        if a < b:
            subtraction = int(b - a)
        else:
            subtraction = a - b
        print("This is your subtraction:", subtraction)
if calculation == str("multiplication"):
    multiplication = a * b 
    print("This is your multiplication:", multiplication)
else:
     if calculation == str("division"): 
        import decimal
        from decimal import Decimal
        if a < b:
            division = decimal.Decimal(b) / decimal.Decimal(a) 
        else:
            division = decimal.Decimal(a) / decimal.Decimal(b)
        print("This is your division:", division)