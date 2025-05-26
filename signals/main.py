from collections import defaultdict

def decode_signals(days):
	mapping = {}
	possible = defaultdict(list)
	
	#collect all possible code-event pairs
	for codes, events in days:
		for code in codes:
			possible[code].append(set(events))
	
	#merge possibilities
	for code in possible:
		common = set.intersection(*possible[code])
		possible[code] = common
	
	progress=True
	while progress:
		progress=False
		for code, events in possible.items():
			if code in mapping:
				continue
			if len(events)==1:
				event=next(iter(events))
				mapping[code]=event
				progress=True
				#remove event from other codes
				for other in possible:
					if other!=code:
						possible[other].discard(event)
      #whyyyyyy no wokr?????
	return mapping

if __name__=="__main__":
	with open('./input.txt','r') as f:
		data=eval(f.read())
	result=decode_signals(data)
	print(result)
