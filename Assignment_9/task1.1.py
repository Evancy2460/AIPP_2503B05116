def sum_even_odd(numbers: list[int]) -> tuple[int, int]:
	"""Return the sum of even and odd integers from a list.

	This function computes two sums from the provided list of integers:
	the sum of all even numbers and the sum of all odd numbers.

	Args:
		numbers (list[int]): A list of integers to process.

	Returns:
		tuple[int, int]: A 2-tuple where the first element is the sum of even
			integers and the second element is the sum of odd integers.

	Raises:
		TypeError: If `numbers` is not an iterable of integers.

	Examples:
		>>> sum_even_odd([1, 2, 3, 4])
		(6, 4)
	"""
	if not hasattr(numbers, '__iter__'):
		raise TypeError('numbers must be an iterable of integers')

	sum_even = 0
	sum_odd = 0

	for i, value in enumerate(numbers):
		if not isinstance(value, int):
			raise TypeError(f'element at index {i} is not int: {value!r}')
		if value % 2 == 0:
			sum_even += value
		else:
			sum_odd += value

	return sum_even, sum_odd


if __name__ == '__main__':
	# Simple demonstration / manual test
	example = [1, 2, 3, 4, 5, 6]
	evens, odds = sum_even_odd(example)
	print(f"Input: {example}")
	print(f"Sum of even numbers: {evens}")
	print(f"Sum of odd numbers: {odds}")

