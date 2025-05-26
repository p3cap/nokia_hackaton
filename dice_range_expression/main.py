dice_sizes = [20, 10, 8, 6, 4, 3, 2]

#tries single and two-dice combos to cover the target range exactly with minimal dice count, applies offset if needed
def dice_combo(min_val, max_val):
	target_range = max_val - min_val + 1
	best = None

	#try single dice combos
	for d1 in dice_sizes:
		for n1 in range(1, 21):
			r1 = n1 * d1 - n1 + 1  #range covered by n1 dice d1
			if r1 >= target_range:
				offset = min_val - n1
				expr = f"{n1}d{d1}"
				if offset > 0:
					expr += f"+{offset}"
				elif offset < 0:
					expr += f"{offset}"
				best = (n1, expr)
				break

	#try combos of two dice types
	for d1 in dice_sizes:
		for n1 in range(1, 21):
			for d2 in dice_sizes:
				for n2 in range(1, 21):
					min_sum = n1 + n2
					max_sum = n1 * d1 + n2 * d2
					span = max_sum - min_sum + 1
					if span < target_range:
						continue
					offset = min_val - min_sum
					if min_sum + offset != min_val or max_sum + offset != max_val:
						continue
					num_dice = n1 + n2
					expr = f"{n1}d{d1}+{n2}d{d2}"
					if offset > 0:
						expr += f"+{offset}"
					elif offset < 0:
						expr += f"{offset}"
					if best is None or num_dice < best[0]:
						best = (num_dice, expr)

	return best[1] if best else "Nincs megoldás"


if __name__ == "__main__": #ha egyensen ezt a fájlt inditjuk el (nem indul el ha esetleg imoprtálva van)
	with open('./input.txt', 'r') as f:
		for line in f:
			min_max = line.strip().split()
			min_val,max_val = int(min_max[0]), int(min_max[1])
			print(dice_combo(min_val, max_val))
