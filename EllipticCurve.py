from FQ import FQ

class EllipticCurve(object):

	def __init__(self, a, b, q):
		self.a = a % q
		self.b = b % q
		self.q = q
		self.Fq = FQ(q)

	def calc_x(self, x):
		return self.Fq.shift(x * x * x + self.a * x + self.b)

	def calc_der_x(self, x):
		return self.Fq.shift(3 * x * x + self.a)

	def belongs(self, point):
		x, y = point
		return self.Fq.shift(y * y) == self.calc_x(x)

	def add(self, el_1, el_2):
		if el_1 == "inf":
			return el_2
		if el_2 == "inf":
			return el_1

		x1, y1 = el_1
		x2, y2 = el_2
		if x1 == x2 and (y1 + y2) % self.q == 0:
			return "inf"

		if x1 != x2:
			m = self.Fq.div(y2 - y1, x2 - x1)
		if x1 == x2:
			m = self.Fq.div(self.calc_der_x(x1), 2 * y1)

		delta = m * m % self.q
		x = (delta - x1 - x2) % self.q
		y = ( -y1 + m * (x1 - x)) % self.q

		return (x, y)

	# generate points belonging to Elliptic Curve.
	# by convention, "inf" is the point of infinity
	def gen_elements(self):
		elements = ["inf"]
		for x in range(self.q):
			for y in range(self.q):
				if self.belongs((x, y)):
					elements.append((x, y))
		return elements

	def __str__(self):
		return 'x^3 + {}x + {} in F_{}'.format(self.a, self.b, self.q)