def tip_calculator(tip_percentage):
    sub_total = float(input("Enter subtotal: "))
    tip = sub_total * tip_percentage/100
    total = tip + sub_total
    print(f"Your tip is {tip} and your total is {total}")

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

def factor_with_argument(number):
    x = 1
    factor = []
    while x <= number:
        if number%x == 0:
            factor.append(x)
            x += 1
        else: 
            x += 1
    return factor

def gcf(x, y):
    