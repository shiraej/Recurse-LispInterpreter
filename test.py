import unittest

from LispParser import lispparser as lp

class TestMakeList(unittest.TestCase):
	
	def test_simple_lisp(self):
		'''
		Tests simplest case
		'''
		data = '(list one two three)'
		result = lp(data)
		self.assertEqual(result, ['list', 'one', 'two', 'three'])

	def test_data_types(self):
		'''
		Tests lispparser can handle strings, floats and integers
		'''
		data = '(list one 2 3.3)'
		result = lp(data)
		self.assertEqual(result, ['list', 'one', 2, 3.3])

	def test_nested_lisp_middle(self):
		'''
		Tests one nested lisp middle item
		'''
		data = '(list 1 (+ 2 3) 4)'
		result = lp(data)
		self.assertEqual(result, ['list', 1, ['+', 2, 3], 4])

	def test_nested_lisp_end(self):
		'''
		Tests one nested lisp middle item
		'''
		data = '(list 1 4 (+ 2 3))'
		result = lp(data)
		self.assertEqual(result, ['list', 1, 4, ['+', 2, 3]])

	def test_two_nested(self):
		'''
		Tests two nested lisp functions
		'''
		data = '(list (+ 1 2) (- 3 4) 5)'
		result = lp(data)
		self.assertEqual(result, ['list', ['+', 1, 2], ['-', 3, 4], 5]) 

	def test_nested_in_nested(self):
		'''
		Tests lisp operation nested in a lisp operation nested in a lisp operation
		'''
		data = '(list (+ (- 1 2) 3) 4 5)'
		result = lp(data)
		self.assertEqual(result, ['list', ['+', ['-', 1, 2], 3], 4, 5])


if __name__ == '__main__':
	unittest.main()
