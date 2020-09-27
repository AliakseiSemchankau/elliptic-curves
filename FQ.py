class FQ(object):

	def __init__(self, q):
		self.q = q
		self.inverse = []
		for i in range(q):
			self.inverse.append(0)
		for a in range(q):
			for b in range(a, q):
				if (a * b) % q == 1:
					self.inverse[a] = b
					self.inverse[b] = a

	def shift(self, x):
		if x < 0:
			t = -x
			t = t % self.q
			x = self.q - t
		return x % self.q

	def div(self, a, b):
		a = self.shift(a)
		b = self.shift(b)
		return self.shift(a * self.inverse[b])