number = int(input("Enter a number to see its multiplication table: "))
result = []
for Y in range(1,11):
    result = number * Y
    print(f"{number} * {Y} = {result}")


