dice_sizes = [20, 10, 8, 6, 4, 3, 2]

def dice_combo(min_val, max_val):
	target_range = max_val - min_val + 1
	best = None  # (number_of_dice, expression)

	for d1 in dice_sizes:
		for n1 in range(1, 21):
			for d2 in [None] + dice_sizes:
				for n2 in range(1, 21 if d2 else 2):
					if d2:
						min_sum = n1 + n2
						max_sum = n1 * d1 + n2 * d2
					else:
						min_sum = n1
						max_sum = n1 * d1

					if max_sum - min_sum + 1 < target_range:
						continue

					offset = min_val - min_sum
					if min_sum + offset == min_val and max_sum + offset == max_val:
						parts = [f"{n1}d{d1}"]
						if d2:
							parts.append(f"{n2}d{d2}")
						expr = '+'.join(parts)
						if offset > 0:
							expr += f"+{offset}"
						elif offset < 0:
							expr += f"{offset}"
						num_dice = n1 + (n2 if d2 else 0)
						if best is None or num_dice < best[0]:
							best = (num_dice, expr)
	return best[1] if best else "Nincs megoldás"

with open('./input.txt', 'r') as f:
	input = f.read()

for line in input.strip().splitlines():
	a, b = map(int, line.strip().split())
	print(dice_combo(a, b))
