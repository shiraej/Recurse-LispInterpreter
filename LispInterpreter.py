def operation(lisplist):
	operator = lisplist[0]
	items = []
	
	''' define operators functions'''
	def addition(items):
		thesum = 0
		for item in items:
			thesum += item
		return thesum
	
	def listing(items):
		thelist = []
		for item in items:
			thelist+=item
		return thelist


	for element in lisplist[1:]:
		if element is list:
			items.append(operation(items))
		else:
			items.append(item)
	if operator == '+':
		return addition(items)

def interpret (lispstring):
	lisplist = lispparser(lispstring)
	return operation(lisplist)

