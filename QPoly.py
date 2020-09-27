import itertools

def gcd(a, b):
   if abs(a) < abs(b):
      return gcd(b, a)
 
   while abs(b) > 0:
      q,r = divmod(a,b)
      a,b = b,r
 
   return a

#generic polynomial in F_q
class QPoly(object):

	def __init__(self, coefs, Fq):
		self.coefs = [c % Fq.q for c in coefs]
		while len(self.coefs) and self.coefs[-1] == 0:
			del self.coefs[-1]

		self.q = Fq.q
		self.Fq = Fq

	# given (c, d), returns c*x^d 
	@staticmethod
	def getPower(c_d, Fq):
		coef, degree = c_d
		coefs = [0 for _ in range(degree + 1)]
		coefs[-1] = coef
		return QPoly(coefs, Fq)

	def isZero(self):
		return self.coefs == []

	def __repr__(self):
		if self.coefs == []:
			return '0'
		monomials = ['{}x^{}'.format(a, i) if i > 0 and a > 1 else \
			         'x^{}'.format(i) if i > 0 and a > 0 else\
			         '{}'.format(a) if i == 0 else\
			         ''\
					 for i, a in enumerate(self.coefs)]
		monomials = [m for m in monomials if len(m)]			 
		return ' + '.join(monomials)

	def __len__(self):
		return len(self.coefs)

	def __abs__(self):
		return len(self.coefs)

	def copy(self):
		return QPoly(self.coefs.copy(), self.Fq)

	def __neg__(self):
		return QPoly([-c for c in self.coefs], self.Fq)

	def __add__(self, other):
		return QPoly([sum(x) for x in \
					itertools.zip_longest(self.coefs, other.coefs, fillvalue=0)], self.Fq)

	def __sub__(self, other):
		return self + (-other)

	def __eq__(self, other):
		return len(self) == len(other) and\
				all([x == y for x, y in zip(self.coefs, other.coefs)])

	def __mul__(self, other):
		if self.isZero() or other.isZero():
			return QPoly([], self.Fq)

		coefs = [0 for _ in range(len(self) + len(other))]
		for i, a in enumerate(self.coefs):
			for j, b in enumerate(other.coefs):
				coefs[i + j] = (coefs[i + j] + a * b) % self.q
		return QPoly(coefs, self.Fq)

	# we implement __divmod__ so that it could be used by gcd
	def __divmod__(self, other):
		quotient, reminder = QPoly([], self.Fq), self.copy()
		while len(reminder) >= len(other):
			lead_coef = self.Fq.div(reminder.coefs[-1], other.coefs[-1])
			lead_power = len(reminder) - len(other)
			lead_monomial = QPoly.getPower((lead_coef, lead_power), self.Fq)
			quotient += lead_monomial
			reminder -= (lead_monomial * other)
		return quotient, reminder 

	def __hash__(self):
		return self.__repr__().__hash__()
