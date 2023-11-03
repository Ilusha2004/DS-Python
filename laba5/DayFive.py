from numpy.polynomial import Polynom
import scipy


# p.roots

def task_one():
     p = Polynomial([0, 2, 3])
     print(p)
     q = p + p
     r = q - p
     r = q // p
     r = q % p
     r = p ** 2
     r = 2 * p
     r = [1, 2] * p
     s = Polynomial.fromroots([1, 1, 2])
     t = p.deriv(2)
     t1 = p.integ(lbnd=1)
     print(t, t1, sep='\n')


if __name__ == "__main__":
     task_one()
