from FQ import FQ
from QPoly import QPoly, gcd
from PowerTerm import PowerTerm

# emulate field of q**d elements
class FQK(object):

	def isIrreducible(self, P):
		T = self.q ** self.d - 1
		for power in range(1, T):
			if T % power != 0:
			  	continue
			SpittingPoly = QPoly.getPower((1, power + 1), self.Fq) -\
		                   QPoly.getPower((1, 1), self.Fq)
			if len(gcd(SpittingPoly, P)) > 1:
				return False
		return True

	def irrPoly(self):
		if self.d == 1:
			return QPoly([0, 1], self.Fq)
		for t in range(self.q ** self.d):
			coefs = []
			for i in range(self.d):
				coefs.append(t % self.q)
				t //= self.q
			irr_poly = QPoly.getPower((1, self.d), self.Fq) + QPoly(coefs, self.Fq) 
			if self.isIrreducible(irr_poly):
				return irr_poly
		print('for {}**{} no irreducible polynomial is found...'.format(self.q, self.d))

	def __init__(self, q, d):
		self.q = q
		self.d = d
		self.Fq = FQ(q)
		self.irr = self.irrPoly()

		# we store mapping i -> (x^i % irreducible)
		self.mult_to_add = [QPoly([1], self.Fq)]

		x = QPoly([0, 1], self.Fq)
		for i in range(1, q ** d - 1):
			P = self.mult_to_add[-1]
			Px = P * x
			_, Px = divmod(Px, self.irr)
			self.mult_to_add.append(Px)
		
		# we store mapping (x^i % irreducible) -> i
		self.add_to_mult = {}
		for i, p in enumerate(self.mult_to_add):
			self.add_to_mult[p] = i

		# mapping (i, j) -> k when x^i + x^j = x^k (mod irreducible)
		self.mult_plus_mult = {}
		for i in range(q ** d - 1):
			qpoly_i = self.mult_to_add[i]
			for j in range(i, q ** d - 1):
				qpoly_j = self.mult_to_add[j]
				self.mult_plus_mult[(i, j)] = self.convert(qpoly_i + qpoly_j).power
				self.mult_plus_mult[(j, i)] = self.mult_plus_mult[(i, j)]

	# convert QPoly to PowerTerm in this field, i.e. modulo self.irr
	def convert(self, qpoly):
		P = qpoly.copy()
		_, P = divmod(P, self.irr)
		if P.isZero():
			return PowerTerm(None, self)
		return PowerTerm(self.add_to_mult[P], self)