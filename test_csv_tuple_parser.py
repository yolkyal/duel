import unittest
import csv_tuple_parser


class TestCsvTupleParser(unittest.TestCase):
	def setUp(self):
		self.csv_tuple_parser = csv_tuple_parser.CsvTupleParser()
		
	def testParse(self):
		file = 'resources/tuples_test.csv'
		
		tuples = self.csv_tuple_parser.parse(file)
		
		expected_tuples = [('s1', 'a1', 's2'), ('s2', 'a2', 's1'), ('s1', '100', 's2'), ('s2', '200', 's1')]
		
		self.assertEqual(expected_tuples, tuples)