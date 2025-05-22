import decimal
from decimal import Decimal
a = str(input("Enter the currency you want to convert lei to - 1 = Euro, 2 = USD, 3 = Pound Sterling:"))
if a == "1":
    b = str(input("Enter the amount of lei you want to convert:"))
    amount = decimal.Decimal(b) / decimal.Decimal(4.97)
    print("This is the converted amount:", format(amount, ".4f"), "euros.")
elif a == "2":
        b = str(input("Enter the amount of lei you want to convert:"))
        amount = decimal.Decimal(b) / decimal.Decimal(4.47)
        print("This is the converted amount:", format(amount, ".4f"), "dollars.")
elif a == "3":
        b = str(input("Enter the amount of lei you want to convert:"))
        amount = decimal.Decimal(b) / decimal.Decimal(6.00)
        print("This is the converted amount:", format(amount, ".4f"), "pounds." )
else:
    print("This is not a currency.")