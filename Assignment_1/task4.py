#!/usr/bin/env python3
"""Assignment 1 — factorial implementations

Provides two working factorial implementations:
- factorial_recursive(n: int) -> int
- factorial_iterative(n: int) -> int

Both validate that n is a non-negative integer.
"""

from __future__ import annotations


def factorial_recursive(n: int) -> int:
    """Return n! computed recursively.

    Args:
        n: non-negative integer

    Returns:
        n! as int

    Raises:
        TypeError: if n is not an int
        ValueError: if n is negative

    Note: recursion depth may be hit for very large n (Python default ~1000).
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """Return n! computed iteratively (loop).

    Args and errors same as factorial_recursive.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    # Interactive factorial calculator
    try:
        while True:
            s = input("Enter a non-negative integer to compute factorial (blank to quit): ").strip()
            if s == "":
                break
            if s.lower() in ("q", "quit", "exit"):
                break
            try:
                n = int(s)
            except ValueError:
                print(f"'{s}' is not an integer")
                continue
            try:
                print(f"{n}! (recursive) = {factorial_recursive(n)}")
                print(f"{n}! (iterative) = {factorial_iterative(n)}")
            except Exception as e:
                print(f"Error: {e}")
    except (EOFError, KeyboardInterrupt):
        print()
    print("Goodbye.")
