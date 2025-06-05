def test(number):
    if number % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")

number = int(input("Enter number: "))
test(number)