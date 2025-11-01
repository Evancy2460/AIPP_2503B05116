import csv
from typing import Optional, Dict


def read_csv_stats(filepath: str, column_name: Optional[str] = None) -> Dict[str, float]:
	"""Read a CSV file and return mean, min, max for a numeric column.

	If `column_name` is None the function will pick the first column that contains
	numeric values. Raises ValueError if no numeric data is found.
	"""
	values = []
	with open(filepath, newline='') as f:
		# Try to read with DictReader (header) first
		f.seek(0)
		dict_reader = csv.DictReader(f)
		if dict_reader.fieldnames:
			rows = list(dict_reader)
			if not rows:
				raise ValueError(f"CSV '{filepath}' has no data rows")

			if column_name is None:
				# find first column with numeric data
				for field in dict_reader.fieldnames:
					vals = []
					for r in rows:
						cell = r.get(field)
						try:
							vals.append(float(cell))
						except Exception:
							continue
					if vals:
						values = vals
						break
				if not values:
					raise ValueError("No numeric column found in CSV")
			else:
				for r in rows:
					cell = r.get(column_name)
					try:
						values.append(float(cell))
					except Exception:
						continue
				if not values:
					raise ValueError(f"No numeric data found in column '{column_name}'")
		else:
			# No header — fallback to reader and collect all numeric cells
			f.seek(0)
			simple_reader = csv.reader(f)
			for row in simple_reader:
				for cell in row:
					try:
						values.append(float(cell))
					except Exception:
						continue
			if not values:
				raise ValueError("No numeric data found in CSV")

	mean_val = sum(values) / len(values)
	return {"mean": mean_val, "min": min(values), "max": max(values)}


if __name__ == '__main__':
	import os

	csv_path = os.path.join(os.path.dirname(__file__), 'data.csv')
	stats = read_csv_stats(csv_path)
	print(f"From {csv_path}: mean={stats['mean']}, min={stats['min']}, max={stats['max']}")

