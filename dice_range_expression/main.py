dice_sizes = [20, 10, 8, 6, 4, 3, 2]

def dice_combo(min_val, max_val):
	expression = None
	dice = None

	for d1 in dice_sizes:
		for n1 in range(1, 11):
			for d2 in [None] + dice_sizes:
				for n2 in range(1, 11 if d2 else 2):
					#raw min/max
					raw_min = n1 + (n2 if d2 else 0)
					raw_max = n1 * d1 + (n2 * d2 if d2 else 0)

					#offset
					for offset in range(-20, 21):
						min_sum = raw_min + offset
						max_sum = raw_max + offset

						if min_sum == min_val and max_sum == max_val:
							parts = [f"{n1}d{d1}"]
							if d2:
								parts.append(f"{n2}d{d2}")
							expr = '+'.join(parts)
							if offset > 0:
								expr += f"+{offset}"
							elif offset < 0:
								expr += f"{offset}"
							num_dice = n1 + (n2 if d2 else 0)
							if expression is None or num_dice < dice:
								expression = expr
								dice = num_dice

	return expression if expression else "Nincs megoldás"

if __name__ == "__main__": #ha egyensen ezt a fájlt inditjuk el (nem indul el ha esetleg imoprtálva van)
	with open('./input.txt', 'r') as f:
		for line in f:
			min_max = line.strip().split()
			min_val,max_val = int(min_max[0]), int(min_max[1])
			print(dice_combo(min_val, max_val))
