class CsvTupleParser:
	def __init__(self):
		pass

	def parse(self, filepath):
		with open(filepath) as f:
			return [tuple(l.rstrip('\n').split(',')) for l in f]
