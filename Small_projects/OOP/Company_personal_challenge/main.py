from Company import Company
from CEO import CEO
from TeamLeader import TeamLeader
from Developer import Developer


def main():
	company = Company({'ios':'levi','windos':'baruch','charge':'baruch','mefathim':'baruch'})
#	
	company.update({'linux':'menachem','offis':'dudi'})
	print(company)
	
	yossi =	TeamLeader('yossi')
	moshe = Developer('moshe', yossi)
	israel = Developer('israel', yossi)
	yossi.adding('game',company)
	print(company)
	yossi.remove('ios', company)
	yossi.remove('linux', company)
	print(company)
	yossi.edit('offis', company)
	yossi.edit('windos', company)
	print(company)
	moshe.adding('store', company)
	moshe.adding('cars', company)
	moshe.adding('airpods', company)
	israel.adding('airtag', company)
	israel.adding('iphone', company)
	israel.adding('pixle', company)
	print(company)
	israel.edit('mefathim',company)
	israel.edit('store', company)
	israel.edit('windos', company)
	moshe.remove('airpods', company)
	moshe.remove('airtag', company)
	moshe.remove('game',company)
	moshe.remove('charge', company)
	print(company)
	
if __name__=='__main__':
	main()
