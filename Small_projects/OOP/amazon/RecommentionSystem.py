from GoldProduct import GoldProduct
from Product import Product

class RecommentionSystem():

	def __init__(self, product_tuples):
		products = {}
		for produc in product_tuples:
			if produc[1] == -1:
				products[produc[0]] = Product(produc[0])
			else:
				products[produc[0]] = GoldProduct(produc[0], produc[1])
		self.products = products
	
	def update(self, purchased_product_names):
		for pro in purchased_product_names:
			self.products[pro].update([prod for prod in purchased_product_names if not prod == pro])
				
	def  get_recommendations(self, product_name, k):
		return self.products[product_name].get_recommendations(k)
