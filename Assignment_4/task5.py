import os


def count_lines_in_file(path):
	"""
	Count the number of lines in a text file.

	Args:
		path (str): Path to the file to read.

	Returns:
		int: Number of lines in the file.

	Raises:
		FileNotFoundError: If the file does not exist.
		IsADirectoryError: If the path is a directory.
		OSError: For other I/O related errors.
	"""
	# Normalize path and quick checks
	if not os.path.exists(path):
		raise FileNotFoundError(f"File not found: {path}")
	if os.path.isdir(path):
		raise IsADirectoryError(f"Path is a directory, not a file: {path}")

	count = 0
	# Use a memory-efficient iteration (line by line)
	with open(path, 'r', encoding='utf-8', errors='replace') as f:
		for _ in f:
			count += 1

	return count


if __name__ == '__main__':
	# Simple CLI loop: ask for file paths until user exits
	print("Line counter. Enter a path to a .txt file (empty to exit).")
	while True:
		try:
			path = input("File path: ").strip()
			if not path:
				print("Goodbye.")
				break

			lines = count_lines_in_file(path)
			print(f"{path} -> {lines} line{'s' if lines != 1 else ''}")

		except FileNotFoundError as e:
			print(e)
		except IsADirectoryError as e:
			print(e)
		except OSError as e:
			print(f"I/O error: {e}")
		except KeyboardInterrupt:
			print("\nInterrupted. Exiting.")
			break
