import math

number = 999983

def primechecker(number):
    for x in range(3,int(math.sqrt(number+1)),2):
        if number % x == 0:
            print("Not a prime")
            return None
    print("Prime")

primechecker(number)
