i = 0
for i in range(0,100):
    i = i + 1
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
    else:
        if i % 3 == 0:
            print ("Fizz")
        else:
            if i % 5 == 0:
                print ("Buzz")
            else:
                print (i)