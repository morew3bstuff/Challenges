for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(f"FizzBuzz [{number}]")
    elif number % 3 == 0:
        print(f"Fizz [{number}]")
    else:
        print(number)
    