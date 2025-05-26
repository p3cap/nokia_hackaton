from collections import defaultdict

#narrows down possible events then repeatedly remove uniquely identified events from other codes, contine unmacthed ones will get ?
def decode_signals(daily_data):
	all_events = set()
	for _, events in daily_data:
		all_events.update(events)

	#create a dict where each code maps to all possible events initially
	possible_map = defaultdict(lambda: set(all_events))

	#narrow down possible events
	for codes, events in daily_data:
		events_set = set(events)
		for code in codes:
			possible_map[code] = possible_map[code].intersection(events_set)

	#repeat removing until no changes
	changed = True
	while changed:
		changed = False
		#find and remove signals which have exactly one possible event
		solved = {code: next(iter(events)) for code, events in possible_map.items() if len(events) == 1}
		for code, event in solved.items():
			for other_code in possible_map:
				if other_code != code and event in possible_map[other_code]:
					possible_map[other_code].remove(event)
					changed = True

	result = {}
	for code, events in possible_map.items():
		if len(events) == 1:
			result[code] = next(iter(events))
		else:
			result[code] = '?'

	return result

if __name__ == "__main__":
	with open('./input.txt', 'r') as f:
		raw = f.read()
	daily_data = eval(raw) 

	decoded = decode_signals(daily_data) #decode the signals
	for k in sorted(decoded):
		print(f"{k}: {decoded[k]}")
