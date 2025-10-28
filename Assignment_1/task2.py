#!/usr/bin/env python3
"""Assignment 1 — primality check

Provides a small, efficient is_prime(n: int) -> bool implementation
and a tiny test harness when run as a script.
"""

def is_prime(n: int) -> bool:
	"""Return True if n is prime, otherwise False.

	- Handles n < 2 (not prime).
	- Uses 6k ± 1 optimization to check divisors up to sqrt(n).
	"""
	if n < 2:
		return False
	if n <= 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i * i <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True


if __name__ == "__main__":
	# Interactive primality checker
	print("Primality checker. Enter integers to test. Type 'q' or blank line to quit.")
	try:
		while True:
			s = input("Enter integer(s) (separate multiple with space or comma): ").strip()
			if s == "" or s.lower() in ("q", "quit", "exit"):
				break
			# allow commas as separators as well
			parts = [p for p in s.replace(',', ' ').split()]
			for p in parts:
				try:
					n = int(p)
				except ValueError:
					print(f"'{p}' is not a valid integer.")
					continue
				print(f"{n}: {'prime' if is_prime(n) else 'composite'}")
	except (EOFError, KeyboardInterrupt):
		# Clean exit on Ctrl-D/Ctrl-C
		print()
	print("Goodbye.")

