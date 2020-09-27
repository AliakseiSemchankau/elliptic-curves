from FQ import FQ
from QPoly import QPoly, gcd
from PowerTerm import PowerTerm
from FQK import FQK

from pprint import pprint

def test_QPoly():
	Fq = FQ(3)

	print('test add')
	test_cases1 = [[0], [1], [1, 2], [3, 2, 1], [1, 1, 1]]
	test_cases2 = [[0], [2, 3], [0], [4, 5, 6], [1, 1, 1]]

	test_ans = ['0', '0', '1 + 2x^1', '1 + x^1 + x^2', '2 + 2x^1 + 2x^2']

	for c1, c2, A in zip(test_cases1, test_cases2, test_ans):
		P1 = QPoly(c1, Fq)
		P2 = QPoly(c2, Fq)
		Q = P1 + P2
		if str(Q) != A:
			print('FAIL: ', P1, ' + ', P2, ' -> ', Q)

	print('test mult')

	test_ans = ['0', '2', '0', '0 + 2x^1 + 2x^2 + 2x^3', '1 + 2x^1 + 2x^3 + x^4']

	for c1, c2, A in zip(test_cases1, test_cases2, test_ans):
		P1 = QPoly(c1, Fq)
		P2 = QPoly(c2, Fq)
		Q = P1 * P2
		if str(Q) != A:
			print('FAIL: ', P1, ' * ', P2, ' -> ', Q)

	print('test div')
	test_cases1 = [QPoly.getPower((1, 27), Fq) - QPoly.getPower((1, 1), Fq),
	               QPoly([1, 1, 1, 1, 1], Fq),
	               QPoly([1, 1], Fq),
	               QPoly([2], Fq),
	               QPoly([1, 2, 1], Fq)]

	test_cases2 = [QPoly([1, 2, 0, 1], Fq), 
	               QPoly([1, 2, 0, 1], Fq),
	               QPoly([2, 1], Fq),
	               QPoly([1], Fq),
	               QPoly([1, 1], Fq)]
	test_ans = ['0', '0 + x^1 + 2x^2', '2', '0', '0']

	for P, Q, A in zip(test_cases1, test_cases2, test_ans):
		quot, rem = divmod(P, Q)
		if str(rem) != A:
			print('FAIL: ', P, ' / ', Q, ' -> ', quot, rem)

	print('test gcd')

	test_ans = ['1 + 2x^1 + x^3', '1', '2', '1', '1 + x^1']
	for P, Q, A in zip(test_cases1, test_cases2, test_ans):
		R = gcd(P, Q)
		if str(R) != A:
			print('FAIL: gcd(', P, ',', Q, ') -> ', R)

def test_PowerTerm():
	q = 3
	d = 2
	Fqd = FQK(q, d)
	ans_add_to_mult = {
		'0 + x^1': 1,
		'1 + 2x^1': 2,
		'2 + 2x^1': 3,
		'2': 4,
		'0 + 2x^1': 5,
		'2 + x^1': 6,
		'1 + x^1': 7,
		'1': 0}
	res_add_to_mult = {str(k) : v for k, v in Fqd.add_to_mult.items()}
	if res_add_to_mult != ans_add_to_mult:
		print('FAIL: FQK({}, {}).add_to_mult = ')
		pprint(Fqd.add_to_mult)

	ans_mult_to_add = ['1', '0 + x^1', '1 + 2x^1', '2 + 2x^1', 
	                   '2', '0 + 2x^1', '2 + x^1', '1 + x^1']
	res_mult_to_add = [str(v) for v in Fqd.mult_to_add]
	if res_mult_to_add != ans_mult_to_add:
		print('FAIL: FQK({}, {}).mult_to_add = ')
		pprint(Fqd.mult_to_add)

	print('test add')

	test_cases = [(0, 1), (2, 3), (4, 2), (8, 3)]
	test_ans = [7, 1, 5, 5]
	for t, a in zip(test_cases, test_ans):
		i, j = t
		PTi = PowerTerm(i, Fqd)
		PTj = PowerTerm(j, Fqd)
		PTk = PTi + PTj
		k = PTk.power 
		if k != a:
			print('FAIL: t^{} + t^{} = t^{}'.format(i, j, k))
			
	print('test truediv')

	test_cases = [(0, 1), (2, 3), (4, 2), (8, 3)]
	test_ans = [7, 7, 2, 5]
	for t, a in zip(test_cases, test_ans):
		i, j = t
		PTi = PowerTerm(i, Fqd)
		PTj = PowerTerm(j, Fqd)
		PTk = PTi / PTj
		k = PTk.power 
		if k != a:
			print('FAIL: t^{} / t^{} = t^{}'.format(i, j, k))

test_QPoly()
test_PowerTerm()
