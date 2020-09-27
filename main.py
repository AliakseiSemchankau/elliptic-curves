from EllipticCurve import EllipticCurve
from FQKEllipticCurve import FQKEllipticCurve
from EllipticCurveGroup import EllipticCurveGroup

def is_prime(p):
	if p == 1:
		return False
	for a in range(2, p):
		if p % a == 0:
			return False
	return True

def main():
	for q in [3, 5, 7, 11, 13, 17, 19, 23, 71]:
		E = EllipticCurve(-1, 0, q)
		ECG = EllipticCurveGroup(E)
		print(q, ECG.group_repr())

	for q_d in [(3, 2), (3, 3), (11, 3)]:
		q, d = q_d
		E = FQKEllipticCurve(-1, 0, q, d)
		ECG = EllipticCurveGroup(E)
		
		print(q**d, ECG.group_repr())

if __name__ == '__main__':
	main()
