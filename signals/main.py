def decode_signal(signal_events):
	sum_up = {} #sums up all possible events wiht duplicates for each signal as a key
	for numbers, letters in signal_events:
		for num in numbers:
			if num not in sum_up: #create list for signal, if there isn't one
				sum_up[num] = [] 
			sum_up[num].extend(letters) # add the possible events to it

	used = []
	decoded = {} #selects most common letters in each list
	
	for code in sorted(sum_up):
		counts = {}
		for letter in sum_up[code]:
			if letter not in counts:
				counts[letter] = 0
			counts[letter] += 1

		#pick the most common letter thats not used yet
		best = None
		best_count = -1
		for letter in counts:
			if letter not in used and counts[letter] > best_count:
				best = letter
				best_count = counts[letter]

		decoded[code] = best if best else '?'
		if best:
			used.append(best)
	return decoded

if __name__ == "__main__": #ha egyensen ezt a fájlt inditjuk el (nem indul el ha esetleg imoprtálva van)
	with open('./input.txt', 'r') as f:
		raw = f.read()

	decoded = decode_signal(eval(raw))
	for k in sorted(decoded):
		print(f"{k}: {decoded[k]}")