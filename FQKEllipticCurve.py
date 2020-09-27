from FQ import FQ
from FQK import FQK

from QPoly import QPoly
from PowerTerm import PowerTerm

class FQKEllipticCurve(object):

	# we keep Elliptic Curve in Weierstrass form yy = xxx + ax + b
	def __init__(self, a, b, q, d):
		self.str = 'x^3 + {}x + {} in F_{}'.format(a % q, b % q, q**d)
		Fq = FQ(q)
		Fqd = FQK(q, d)
		self.q = q
		self.d = d
		self.Fq = Fq
		self.Fqd = Fqd
		self.a = Fqd.convert(QPoly([a % q], Fq))
		self.b = Fqd.convert(QPoly([b % q], Fq))
		self.two = self.Fqd.convert(QPoly([2], self.Fq))
		self.three = self.Fqd.convert(QPoly([3], self.Fq))

	def calc_x(self, x):
		return x * x * x + self.a * x + self.b

	def calc_der_x(self, x):
		return self.three * x * x + self.a

	def belongs(self, point):
		if point == "inf":
			return True
		x, y = point
		return y * y == self.calc_x(x)

	# add two points on Elliptic Curve
	def add(self, el_1, el_2):
		if el_1 == "inf":
			return el_2
		if el_2 == "inf":
			return el_1

		x1, y1 = el_1
		x2, y2 = el_2
		if x1 == x2 and (y1 + y2).isZero():
			return "inf"

		if x1 != x2:
			m = (y2 - y1) / (x2 - x1)
		if x1 == x2:
			m = self.calc_der_x(x1) / (self.two * y1)

		delta = m * m
		x = delta.copy()
		x = x - (x1 + x2)

		y = -y1 + m * (x1 - x)

		return (x, y)

	def __str__(self):
	 	return self.str

	# generate points belonging to Elliptic Curve.
	# by convention, "inf" is the point of infinity
	def gen_elements(self):
		elements = ["inf"]
		x_values = [PowerTerm(t, self.Fqd) for t in range(self.q ** self.d - 1)]
		x_values.append(PowerTerm(None, self.Fqd))
		for x in x_values:
			# value xxx + ax + b
			val = self.calc_x(x)
			# if value = zero
			if val.power is None:
				y = PowerTerm(None, self.Fqd)
				elements.append((x, y))
				continue
			# if value is perfect square, y = +-sqrt(value)
			if val.power % 2 == 0:
				y = PowerTerm(val.power // 2, self.Fqd)
				elements.append((x, y))
				elements.append((x, -y))
		return elements




