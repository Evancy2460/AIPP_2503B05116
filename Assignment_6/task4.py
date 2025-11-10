def sum_to_n(n: int, method: str) -> int:
    method_key = method.strip().lower()
    match method_key:
        case "for":
            total = 0
            for i in range(1, n + 1):
                total += i
            return total
        case "while":
            total = 0
            i = 1
            while i <= n:
                total += i
                i += 1
            return total
        case _:
            raise ValueError("Unknown method. Use 'for' or 'while'.")


if __name__ == "__main__":
    try:
        n_val = int(input("Enter n (positive integer): "))
        method = input("Choose method ('for' or 'while'): ")
        print(sum_to_n(n_val, method))
    except ValueError as exc:
        print(f"Error: {exc}")

