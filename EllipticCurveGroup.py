from collections import defaultdict

def get_orbit(el, table):
	orbit = ["inf"]
	el_power = el
	while el_power != "inf":
		orbit.append(el_power)
		el_power = table[(el_power, el)]
	return orbit

# returns group <g_1, g_2, ...>, g_i \in generators
def write_products(elements, table, generators):
	element_to_product = defaultdict(list)
	H = ["inf"]
	inf_order = []
	for i in range(len(generators)):
		inf_order.append(0)
	element_to_product["inf"] = inf_order

	for i, g in enumerate(generators):
		Hg = H.copy()
		for k, g_o in enumerate(get_orbit(g, table)):
			if k == 0:
				continue
			for h in H:
				gkh = table[(g_o, h)]
				Hg.append(gkh)
				element_to_product[gkh] = element_to_product[h].copy()
				element_to_product[gkh][i] += k
		H = Hg

	return element_to_product

def gen_table(elements, E):
	table = {}
	for i in range(len(elements)):
		el_1 = elements[i]
		for j in range(i, len(elements)):
			el_2 = elements[j]
			add = E.add(el_1, el_2)
			table[(el_1, el_2)] = add
			table[(el_2, el_1)] = add
	return table

def gen_orders(elements, table):
	orders = {}
	for el in elements:
		orders[el] = len(get_orbit(el, table))
	return orders

# return (#prime divisors of x, #least prime, #x).
# used to order generators of the group, later.
def w_num(x):
	if x == 1:
		return (100, 0, 0)
	num = x
	primes = []
	for p in range(2, x + 1):
		if x % p == 0:
			while x % p == 0:
				primes.append(p)
				x //= p
	return (len(set(primes)), primes[0], -num)

def gen_generators(elements, table, orders):
	if len(elements) == 1:
		return ["inf"]
	generators = []
	elements = sorted(elements, key=lambda x: w_num(orders[x]))
	H = set(["inf"])
	for g in elements:
		if g == "inf":
			continue
		g_orbit = get_orbit(g, table)
		is_independent = True
		# we assume the first element of the orbit to be "inf"
		for g_power in g_orbit[1:]:
			if g_power in H:
				is_independent = False
				break
		if not is_independent:
			continue
		generators.append(g)
		Hg = set()
		for g_power in g_orbit:
			for h in H:
				Hg.add(table[(g_power, h)])
		H = Hg
	return generators

class EllipticCurveGroup(object):

	def __init__(self, E):
		elements = E.gen_elements()
		table = gen_table(elements, E)
		orders = gen_orders(elements, table)
		generators = gen_generators(elements, table, orders)
		element_to_product = write_products(elements, table, generators)

		self.E = E
		self.elements = elements
		self.table = table
		self.orders = orders
		self.generators = generators
		self.element_to_product = element_to_product

	def group_repr(self):
		return ' ⊕ '.join(['Z_{}'.format(self.orders[g])\
		                                 for g in self.generators])

	def __str__(self):
		s = str(self.E) + '\n'
		s += 'group size : {}\n'.format(len(self.elements))
		s += 'generators:\n' + '\n'.join([' ord({}) = {}'.format(g, self.orders[g])\
		                                  for g in self.generators]) + '\n'

		s += 'group(E) ~ ' + ' ⊕ '.join(['Z_{}'.format(self.orders[g])\
		                                 for g in self.generators])
		return s
