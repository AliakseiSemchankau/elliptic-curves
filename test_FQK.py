from FQ import FQ
from QPoly import QPoly, gcd
from FQK import FQK
from pprint import pprint

def test_irr():
	print('test irr')
	test_cases = [(3, 2), (3, 3), (3, 4), (3, 5),
	              (5, 2), (5, 3), (5, 4),
	              (7, 2), (7, 3),
	              (11, 2), (11, 3)]

	test_ans = ['2 + x^1 + x^2', '1 + 2x^1 + x^3', '2 + x^1 + x^4', '1 + 2x^1 + x^5',
				'2 + x^1 + x^2', '2 + 3x^1 + x^3', '2 + 2x^1 + x^2 + x^4',
				'3 + x^1 + x^2', '2 + 3x^1 + x^3',
	            '7 + x^1 + x^2', '4 + x^1 + x^3']

	for q_d, ans in zip(test_cases, test_ans):
		q, d = q_d
		Fqd = FQK(q, d)
		irr = Fqd.irrPoly()
		if str(irr) != ans:
			print('FAIL: irr(', q, d, ') -> ', irr)

test_irr()
