This project is dedicated to emulate the behaviour 
of groups on elliptic curves in finite fields.

Namely, file main.py contains the solution to §I.9.2
in Nail Koblitz book "Introduction to Elliptic Curves and Modular Forms".

Classes FQ and FQK correspond to fields F_q and F_{q**d}, respectively.
Creating of instance of the second one includes inner creating of irreducible 
polynomial of degree d, etc.
Once the instance of FQ or FQK is created, it is supposed to be used throughtout 
the program. In particular, instance of FQK is being provided to each instance of
class PowerTerm, while FQ is provided to class QPoly.

Class QPoly reflects general polynomial in F_q, while each instance of PowerTerm
reflects element x^i in F_{q**d} or zero in the same field.

Class EllipticCurve works with Elliptic Curves in field F_q.
Instance EllipticCurve(a, b, q) corresponds to y*y = x*x*x + a*x + b in F_q.
Point on EllipticCurve belong to F_q x F_q.

Class FQKEllipticCurve works in F_{q ** d} for d > 1.
Instance FQKEllipticCurve(a, b, q, d) corresponds to y*y = x*x*x + a*x + b in F_{q**d}.
Points on FQKEllipticCurve belong to F_{q**d} x F_{q**d}.

Both this classes have method add (which adds any two points on the curve), and 
get_elements (which enumerates all points on the curve).

To emulate the group , one provides instance of either EllipticCurve or FQKEllipticCurve
to instance of EllipticCurveGroup, which does the following:
1) gets all elements from the curve;
2) create the multiplication table point x point -> point, using elements and method add
from the curve;
3) calculates orders of all elements;
4) as any finite Abelian group (and group of elliptic curve points clearly is) might
be represented as Prod {Z_n}, where n are prime power, we find generators of each 
such Z_n;
5) finally, we write mapping point -> g_1^k_1 * g_2^k_2 * ... * g_t^k_t to field 
"element_to_product", where g_1, g_2, ..., g_t are generators.

In file main.py we obtain those representations of group induced by y*y = x*x*x - x
in the following fields:
F_3    : Z_2 ⊕ Z_2
F_5    : Z_4 ⊕ Z_2
F_7    : Z_4 ⊕ Z_2
F_11   : Z_2 ⊕ Z_2 ⊕ Z_3
F_13   : Z_4 ⊕ Z_2
F_17   : Z_4 ⊕ Z_4
F_19   : Z_2 ⊕ Z_2 ⊕ Z_5
F_23   : Z_4 ⊕ Z_2 ⊕ Z_3
F_71   : Z_4 ⊕ Z_2 ⊕ Z_9
F_9    : Z_4 ⊕ Z_4
F_27   : Z_2 ⊕ Z_2 ⊕ Z_7
F_1331 : Z_2 ⊕ Z_2 ⊕ Z_9 ⊕ Z_37


