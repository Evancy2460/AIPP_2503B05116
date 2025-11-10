def print_multiples(number: int) -> None:
    for i in range(1, 11):
        print(number * i)


if __name__ == "__main__":
    # Take number from keyboard and print first 10 multiples
    number = int(input("Enter a number: "))
    print_multiples(number)

