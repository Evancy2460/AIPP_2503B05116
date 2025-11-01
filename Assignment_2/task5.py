
from typing import Iterable, Dict


def sum_even_odd(numbers: Iterable[int]) -> Dict[str, int]:
	"""Return the sum of even and odd integers from `numbers`.

	Args:
		numbers: an iterable of integers (or floats that represent integers).

	Returns:
		dict with keys 'even_sum' and 'odd_sum'.

	Raises:
		ValueError: if any item is not an integer (or integral float).
	"""
	even_sum = 0
	odd_sum = 0
	for item in numbers:
		# Accept integral floats by converting them to int
		if isinstance(item, float):
			if item.is_integer():
				n = int(item)
			else:
				raise ValueError(f"Non-integral number: {item}")
		elif isinstance(item, int):
			n = item
		else:
			raise ValueError(f"Non-integer value: {item}")

		if n % 2 == 0:
			even_sum += n
		else:
			odd_sum += n

	return {"even_sum": even_sum, "odd_sum": odd_sum}


def _parse_ints_from_string(s: str):
	"""Parse space-separated integers from a string; raise ValueError on bad tokens."""
	parts = s.strip().split()
	if not parts:
		return []
	return [int(p) for p in parts]


if __name__ == '__main__':
	try:
		raw = input('Enter integers separated by spaces (or press Enter for none): ')
	except EOFError:
		print('No input received.')
	else:
		try:
			nums = _parse_ints_from_string(raw)
		except ValueError:
			print('Error: please enter valid integers separated by spaces.')
		else:
			result = sum_even_odd(nums)
			print(f"Sum of even numbers: {result['even_sum']}")
			print(f"Sum of odd numbers: {result['odd_sum']}")

