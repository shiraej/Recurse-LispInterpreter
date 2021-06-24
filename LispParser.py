def isnumber(string):
	'''str -> int or float or str
	checks whether the string is a number and what kind (int or float) returns it in that type'''
	try:
		int(string)
		return int(string)
	except ValueError:
		try:
			float(string)
			return float(string)
		except ValueError:
			return string


def makelist(string):
	''' str -> [list, int]
	recursive function that parses Lisp code into an abstract syntax tree returned as a python list'''
	newspot = 0
	counter = 1
	word = ''
	lst=[]
	for char in string[1:]:
		if counter<= newspot:		#this part just fast forwards through the nested lisp operations already seen to through recursion
			counter+=1
			continue
		elif char == '(':
			newstring = string[counter:]
			nestedlisp = makelist(newstring)	#when it encounters the start of a new lisp operation, it calls itself
			lst.append(nestedlisp[0])
			newspot = counter + nestedlisp[1]	#for tracking where we are in the string after returning the recursion
			counter+=1
		elif char == ' ':
			if string[counter-1] == ')': 
				counter+=1
				continue

			else:
				lst.append(isnumber(word))
				word = ''
			counter +=1
		elif char == ')':
			if word !='':		#this is necessary for when two brackets: )) appear as word will be assigned an empty string for the second bracket
				lst.append(isnumber(word))
			word = ''
			return [lst, counter]
		else:
			word += char
			counter +=1

def lispparser(string):
	'''str->list
	just cleans up the result of the makelist function so only the list is returned'''
	return makelist(string)[0]




