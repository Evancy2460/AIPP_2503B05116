import re
from typing import Any
def is_palindrome(s: Any) -> bool:
	"""Return True if string `s` is a palindrome.

	Behaviour / contract:
	- Accepts any input; converts it to string.
	- Ignores non-alphanumeric characters.
	- Is case-insensitive.
	"""
	if s is None:
		return False
	text = str(s)
	# keep only alphanumeric characters and make lowercase
	filtered = re.sub(r'[^0-9a-zA-Z]', '', text).lower()
	return filtered == filtered[::-1]
if __name__ == '__main__':
	# Loop: repeatedly read input from the keyboard and print whether it's a palindrome.
	# Type 'quit' or 'exit' (case-insensitive) to stop, or send EOF (Ctrl+Z then Enter on Windows).
	prompt = "Enter text to check for palindrome (or type 'quit' to exit): "
	while True:
		try:
			s = input(prompt)
		except EOFError:
			print('\nEOF received — exiting.')
			break

		if s is None:
			# should not happen with input(), but handle defensively
			print('No input received — exiting.')
			break

		if s.strip().lower() in ('quit', 'exit'):
			print('Exit command received — exiting.')
			break
		result = is_palindrome(s)
		print(f'Palindrome: {result}\n')

