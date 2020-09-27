# monomial x^i in field F_{q**d} modulo irreducible
class PowerTerm(object):

	# we create monomial x^power
	def __init__(self, power, Fqd):
		self.q = Fqd.q
		self.d = Fqd.d
		self.power = power
		if power is not None:
			self.power %= (self.q ** self.d - 1)
		self.Fqd = Fqd

	def copy(self):
		return PowerTerm(self.power, self.Fqd)

	def isZero(self):
		return self.power is None

	def __len__(self):
		if self.power is None:
			return 0
		return self.power

	def __eq__(self, other):
		return self.power == other.power

	# x^i + x^j = x^k, and mapping (i, j) -> k is precalculated in self.field
	def __add__(self, other):
		if self.power is None:
			return other.copy()
		if other.power is None:
			return self.copy()
		power = self.Fqd.mult_plus_mult[(self.power, other.power)]
		return PowerTerm(power, self.Fqd)

	# -x^i = x^{i + field.size/2}
	def __neg__(self):
		if self.power is None:
			return self.copy()
		return PowerTerm(self.power + (self.q ** self.d - 1) // 2, self.Fqd)

	def __sub__(self, other):
		return self + (-other)

	# x^i * x^j = x^{(i + j) % field.size}
	def __mul__(self, other):
		if self.power is None:
			return self.copy()
		if other.power is None:
			return other.copy()
		power = (self.power + other.power) % (self.q ** self.d - 1)
		return PowerTerm(power, self.Fqd)

	# x^i / x^j = x^{(i - j) % field.size}
	def __truediv__(self, other):
		if self.power is None:
			return self.copy()
		power = (self.power - other.power) % (self.q ** self.d - 1)
		return PowerTerm(power, self.Fqd)

	def __str__(self):
		if self.power is None:
			return 'zero'
		return 't^{}'.format(self.power)

	def __repr__(self):
		return self.__str__()

	def __hash__(self):
		return self.__str__().__hash__()


