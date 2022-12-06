from Product import Product

class GoldProduct(Product):
	
	def __init__(self, product_name, amount, bought_with = {}):
		Product.__init__(self, product_name, bought_with)
		self.amount = amount
		
	def __repr__(self):
		return f'{product.__repr__(self)} ({self.amount} units left!)'

		
	def update(self, product_names):
		Product.update(self, product_names)
		self.amount -=1
	
	def get_recommendations(self, k):
		return [product for product in Product.get_recommendations(self,k) if self.bought_with[product] > 10]

