try:
    number = int(input("Enter a number: "))
    print(number)

    answer=10/0

except ValueError as err1:
    print(err1)
except ZeroDivisionError as err:
    print("You divided by zero here")