from RecommentionSystem import RecommentionSystem


def main():
#	a = product('ab')
	'''	
	b = product('game', {'v':2, 'd':3, 'c':5})
	b.update({'car', 'a'})
	b.update({'car', 'a'})
	b.update({'car', 'a'})
	b.update({'car', 'a'})
	b.update({'car', 'a'})
	b.update({'car', 'a'})
	b.update({'car', 'a'})
		
	
	c = GoldProduct('game', 6, {'v':2, 'd':3, 'c':5, 's':12})
	
	print(c.get_recommendations(2))
	print(c)
	'''
	a = RecommentionSystem([('game', 9), ('xsd', -1), ('car', -1), ('galaxy',15)])
	#print(a.products)
	a.update(['car', 'xsd', 'game'])
	a.update(['car', 'xsd', 'game'])
	a.update(['car', 'xsd', 'game'])
	a.update(['car', 'xsd', 'game'])
	a.update(['car', 'xsd', 'game'])
	a.update(['galaxy', 'xsd', 'game'])
	a.update(['car', 'galaxy', 'game'])
	a.update(['car', 'xsd', 'game'])
	a.update(['car', 'xsd', 'galaxy'])
	a.update(['car', 'galaxy', 'game'])
	a.update(['car', 'xsd', 'game'])	
	z = a.get_recommendations('xsd',2)
	print(z)
	

if __name__=='__main__':
	main()
