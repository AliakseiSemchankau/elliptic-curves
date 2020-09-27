from FQ import FQ
from EllipticCurve import EllipticCurve
from EllipticCurveGroup import gen_table, gen_orders, gen_generators, write_products

from pprint import pprint

def test_div():
	print('test div')
	test_cases = [(11, 7, 5), (-101, 7, 5), (4, 7, 5),
	              (-7, 7, 5), (0, 7, 5), (7, 7, 5)]
	test_anses = [3, 2, 2,
	              4, 0, 1]
	for i, case_ans in enumerate(zip(test_cases, test_anses)):
		case, ans = case_ans
		a, b, q = case
		Fq = FQ(q)
		res = Fq.div(a, b)
		if res != ans:
			print('failed ', a, b, q, ' -> ', res)

def test_gen_table():
	print('test gen_table')
	q = 7
	E = EllipticCurve(-1, 0, q)
	elements = E.gen_elements()
	res_table = gen_table(elements, E)
	ans_table = {('inf', 'inf'): 'inf',
				 ('inf', (0, 0)): (0, 0),
				 ('inf', (1, 0)): (1, 0),
				 ('inf', (4, 2)): (4, 2),
				 ('inf', (4, 5)): (4, 5),
				 ('inf', (5, 1)): (5, 1),
				 ('inf', (5, 6)): (5, 6),
				 ('inf', (6, 0)): (6, 0),
				 ((0, 0), 'inf'): (0, 0),
				 ((0, 0), (0, 0)): 'inf',
				 ((0, 0), (1, 0)): (6, 0),
				 ((0, 0), (4, 2)): (5, 1),
				 ((0, 0), (4, 5)): (5, 6),
				 ((0, 0), (5, 1)): (4, 2),
				 ((0, 0), (5, 6)): (4, 5),
				 ((0, 0), (6, 0)): (1, 0),
				 ((1, 0), 'inf'): (1, 0),
				 ((1, 0), (0, 0)): (6, 0),
				 ((1, 0), (1, 0)): 'inf',
				 ((1, 0), (4, 2)): (4, 5),
				 ((1, 0), (4, 5)): (4, 2),
				 ((1, 0), (5, 1)): (5, 6),
				 ((1, 0), (5, 6)): (5, 1),
				 ((1, 0), (6, 0)): (0, 0),
				 ((4, 2), 'inf'): (4, 2),
				 ((4, 2), (0, 0)): (5, 1),
				 ((4, 2), (1, 0)): (4, 5),
				 ((4, 2), (4, 2)): (1, 0),
				 ((4, 2), (4, 5)): 'inf',
				 ((4, 2), (5, 1)): (6, 0),
				 ((4, 2), (5, 6)): (0, 0),
				 ((4, 2), (6, 0)): (5, 6),
				 ((4, 5), 'inf'): (4, 5),
				 ((4, 5), (0, 0)): (5, 6),
				 ((4, 5), (1, 0)): (4, 2),
				 ((4, 5), (4, 2)): 'inf',
				 ((4, 5), (4, 5)): (1, 0),
				 ((4, 5), (5, 1)): (0, 0),
				 ((4, 5), (5, 6)): (6, 0),
				 ((4, 5), (6, 0)): (5, 1),
				 ((5, 1), 'inf'): (5, 1),
				 ((5, 1), (0, 0)): (4, 2),
				 ((5, 1), (1, 0)): (5, 6),
				 ((5, 1), (4, 2)): (6, 0),
				 ((5, 1), (4, 5)): (0, 0),
				 ((5, 1), (5, 1)): (1, 0),
				 ((5, 1), (5, 6)): 'inf',
				 ((5, 1), (6, 0)): (4, 5),
				 ((5, 6), 'inf'): (5, 6),
				 ((5, 6), (0, 0)): (4, 5),
				 ((5, 6), (1, 0)): (5, 1),
				 ((5, 6), (4, 2)): (0, 0),
				 ((5, 6), (4, 5)): (6, 0),
				 ((5, 6), (5, 1)): 'inf',
				 ((5, 6), (5, 6)): (1, 0),
				 ((5, 6), (6, 0)): (4, 2),
				 ((6, 0), 'inf'): (6, 0),
				 ((6, 0), (0, 0)): (1, 0),
				 ((6, 0), (1, 0)): (0, 0),
				 ((6, 0), (4, 2)): (5, 6),
				 ((6, 0), (4, 5)): (5, 1),
				 ((6, 0), (5, 1)): (4, 5),
				 ((6, 0), (5, 6)): (4, 2),
				 ((6, 0), (6, 0)): 'inf'}

	if res_table != ans_table:
		print('failed ', E, q, ' -> ')
		pprint(res_table)

def test_gen_orders():
	print('test gen_orders')
	q = 7
	E = EllipticCurve(-1, 1, q)
	elements = E.gen_elements()
	table = gen_table(elements, E)
	res_orders = gen_orders(elements, table)
	ans_orders = {'inf': 1,
				 (0, 1): 4,
				 (0, 6): 4,
				 (1, 1): 12,
				 (1, 6): 12,
				 (2, 0): 2,
				 (3, 2): 3,
				 (3, 5): 3,
				 (5, 3): 12,
				 (5, 4): 12,
				 (6, 1): 6,
				 (6, 6): 6}

	if res_orders != ans_orders:
		print('failed ', E, q, ' -> ')
		pprint(res_orders)

def test_gen_generators():
	print('test gen_generators')
	q = 7
	E = EllipticCurve(-1, 0, q)
	elements = E.gen_elements()
	table = gen_table(elements, E)
	orders = gen_orders(elements, table)
	res_generators = gen_generators(elements, table, orders)
	ans_generators = [(4, 2), (0, 0)]
	if sorted(res_generators) != sorted(ans_generators):
		print('failed ', E, q, ' -> ')
		pprint(res_generators)


def test_write_products():
	print('test write_products')
	q = 7
	E = EllipticCurve(-1, 0, q)
	elements = E.gen_elements()
	table = gen_table(elements, E)
	orders = gen_orders(elements, table)
	generators = gen_generators(elements, table, orders)
	element_to_product = write_products(elements, table, generators)
	ans_etp = {'inf': [0, 0],
             (0, 0): [0, 1],
             (1, 0): [2, 0],
             (4, 2): [1, 0],
             (4, 5): [3, 0],
             (5, 1): [1, 1],
             (5, 6): [3, 1],
             (6, 0): [2, 1]}

	if dict(element_to_product) != ans_etp:
		print('failed ', E, q, ' -> ')
		pprint(element_to_product)

test_div()
test_gen_table()
test_gen_orders()
test_gen_generators()
test_write_products()