import math

class Rational:

	def __init__(self, numerator, denominator=1):
		if denominator == 0:
			raise ValueError('denominator is equal to 0')
		self.numerator = numerator
		self.denominator = denominator
	
	def __repr__(self):
		return f'{self.numerator} / {self.denominator}'
	
	
	def add(self, rational):
		numerator = self.numerator * rational.denominator + rational.numerator * self.denominator
		denominator = self.denominator * rational.denominator
		return Rational(numerator, denominator).shrink()
	
	def is_equal(rational):
		return self.numerator/self.denominator == rational.numerator/rational.denominator
	
	def shrink(self):
		gcd = math.gcd(self.numerator, self.denominator)
		return Rational(self.numerator / gcd, self.denominator / gcd)
		
		
def main():

	c1 = Rational(264,450)
	c2 = Rational(7,11)
	c3 = c1.add(c2)
	print(c3)
	c4 = c1.shrink()
	print(c4)
	
if __name__ == '__main__':
	main()
