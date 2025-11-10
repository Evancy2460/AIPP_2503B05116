def print_multiples_while(number: int) -> None:
    i = 1
    while i <= 10:
        print(number * i)
        i += 1


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print_multiples_while(n)

