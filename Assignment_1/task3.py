#!/usr/bin/env python3
"""Assignment 1 — small helpers

This file demonstrates a simple reverse-string function.
"""

# Function to reverse a string
def reverse_string(s: str) -> str:
	"""Return a new string which is the reverse of `s`.

	This was auto-completed (Copilot-like) and uses Python slicing.
	"""
	return s[::-1]


if __name__ == "__main__":
	# Interactive demo: repeatedly ask user for strings to reverse.
	print("Reverse-string demo. Enter text to reverse. Type 'q' or blank line to quit.")
	try:
		while True:
			s = input("Enter string (or 'q' to quit): ")
			if s == "" or s.lower() in ("q", "quit", "exit"):
				break
			print(reverse_string(s))
	except (EOFError, KeyboardInterrupt):
		# clean exit on Ctrl-D/Ctrl-C
		print()
	print("Goodbye.")

