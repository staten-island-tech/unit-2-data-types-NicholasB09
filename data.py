def tip_calculator():
    bill = float(input("Enter bill: "))
    tip_percentage = int(input("Enter tip percentage: "))
    tip = tip_percentage/100 * bill
    total = tip + bill
    print(f"Your total is {total}.")



def word_count():
    sentence = str.split(input("Enter a sentence: "))
    words = 0
    for word in sentence:
        words += 1
    print(words)

def odd_or_even():
    number = int(input("Give me a number: "))
    if number%2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

def tip_based_on_performance():
    x = 0
    bill = int(input("Enter your bill: "))
    while x == 0:
        service_a = input("How good was the service(bad, okay, good, great): ")
        service = service_a.lower()
        if service == "bad":
            print("Don't pay a tip lol")
            x = 1
        elif service == "okay":
            print(f"Your tip is ${bill * 0.15}.")
            x = 1
        elif service == "good":
            print(f"Your tip is ${bill * 0.2}.")
            x = 1
        elif service == "great":
            print(f"Your tip is ${bill * 0.25}.")
            x = 1
        else:
            print("You didn't enter one of the options you dingus.")

# calculator of all factors of a given number

def factors():
    number = int(input("Enter your number: "))
    x = 1
    factor = []
    while x <= number:
        if number%x == 0:
            factor.append(x)
            x += 1
        else: 
            x += 1
    print(factor)

# greatest common factor of two numbers calculator

def gcf(x, y):
    a = 1
    x_factors = []
    while a <= x:
        if x%a == 0:
            x_factors.append(a)
            a += 1
        else:
            a += 1
    b = 1
    y_factors = []
    while b <= x:
        if y%b == 0:
            y_factors.append(b)
            b += 1
        else:
            b += 1
    gcf = 0
    for factor in x_factors:
        if factor in y_factors:
            gcf = factor
    print(f"The gcf of {x} and {y} is: {gcf}")

gcf(69, 24)