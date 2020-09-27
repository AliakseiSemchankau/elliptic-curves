from FQKEllipticCurve import FQKEllipticCurve
from EllipticCurve import EllipticCurve

from pprint import pprint


def test_FQ_gen_elements():
	print('test gen_elements')

	test_cases = [(EllipticCurve(1, 1, 7), 7),
	              (EllipticCurve(-9, 0, 19), 19)]
	test_anses = [['inf', (0, 1), (0, 6), (2, 2), (2, 5)],
	              ['inf', (0, 0), (1, 7), (1, 12), (2, 3), 
	              (2, 16), (3, 0), (4, 3), (4, 16), (5, 2), 
	              (5, 17), (10, 6), (10, 13), (11, 4), (11, 15), 
	              (12, 9), (12, 10), (13, 3), (13, 16), (16, 0)]
	             ]

	for i, case_ans in enumerate(zip(test_cases, test_anses)):
		case, ans = case_ans
		E, q = case
		res = E.gen_elements()
		if res != ans:
			print('failed ', E, q, ' -> ', res)

def test_FQK_gen_elements():
	print('test gen_elements')

	test_cases = [(FQKEllipticCurve(1, 1, 5, 2), 5, 2),
	              (FQKEllipticCurve(1, 1, 7, 2), 7, 2)]
	test_anses = [27, 55]

	for case, ans in zip(test_cases, test_anses):
		E, q, d = case
		res = E.gen_elements()
		if len(res) != ans:
			print('failed ', E, q, d, ' -> ', len(res))

test_FQ_gen_elements()
test_FQK_gen_elements()
