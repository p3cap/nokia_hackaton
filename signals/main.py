from collections import defaultdict

def decode_signals(days):
	mapping = {} #discovered
	possible = defaultdict(list)#new keys will get [] as their basic value
	
	#collect all possible code-event pairs
	for codes, events in days:
		for code in codes:
			possible[code].append(set(events)) #set for easier pairing
	
	#merge possibilities
	for code in possible:
		common = set.intersection(*possible[code])#unpacking the list -> separate {} arguments (for intersection)
		possible[code] = common
	
	progress=True
	while progress:
		progress=False #turns back true in the loop when a signal has 1 sulution
		for code, events in possible.items():
			if code in mapping:
				continue
			if len(events)==1:
				event=next(iter(events)) #gets the first (and only, bc of the merging) element from the set
				mapping[code]=event
				progress=True
				#remove event from other codes
				for other in possible:
					if other!=code:
						possible[other].discard(event)
			#whyyyyyy no wokr?????
	return mapping

if __name__=="__main__":#ha egyensen ezt a fájlt inditjuk el (nem indul el ha esetleg imoprtálva van)
	with open('./input.txt','r') as f:
		data=eval(f.read())
	result=decode_signals(data)
	print(result)

"""
manual matching:
{
	'5.9.1':'A',
	'9.3.8':'I',
	'3.9':'G',
	'8':'D',
	'1':'G',
	'6':'C',
	'3.8':'F',
	'6.7.4':'H',
	'7.1.8':'B',
	'8.6.4':'D',
	'7.4':'H'
}
"""