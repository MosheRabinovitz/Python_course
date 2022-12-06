class Product:
	
	def __init__(self, product_name, bought_with = {}):
		if len(product_name) < 2:
			raise ValueError('invalid name')
		self.product_name = product_name 
		self.bought_with = bought_with.copy()
		
	def __repr__(self):
		return self.product_name
		
	def update(self, product_names):
		for product in product_names:
			self.bought_with[product] = self.bought_with.get(product,0)+1
	
	def get_recommendations(self, k):
		return sorted(self.bought_with, key=self.bought_with.get, reverse=True)[:k]




