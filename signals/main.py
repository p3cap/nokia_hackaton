from collections import Counter

def decode_signal(signal_events):
	sum_up = {}  # signal -> all possible events (with duplicates)

	for numbers, letters in signal_events:
		for num in numbers:
			if num not in sum_up:
				sum_up[num] = []
			sum_up[num].extend(letters)

	decoded = {}
	used_events = set()

	while len(decoded) < len(sum_up):
		progress = False

		for signal, events in sum_up.items():
			if signal in decoded:
				continue

			counts = Counter(e for e in events if e not in used_events)
			if not counts:
				continue

			# Pick the most common remaining event
			event, _ = counts.most_common(1)[0]
			decoded[signal] = event
			used_events.add(event)
			progress = True

		if not progress:
			break

	return decoded

if __name__ == "__main__":
	with open("input.txt", "r") as f:
		raw = f.read()

	decoded = decode_signal(eval(raw))
	for k in sorted(decoded):
		print(f"{k}: {decoded[k]}")
