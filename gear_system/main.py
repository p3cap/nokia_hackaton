def get_instruction(line):
  try:
    target, limit = eval(line.strip()), 8
  except:
    parts = line.strip().split("]")
    target = eval(parts[0] + "]")
    limit = int(parts[1].strip())
  return target, limit

def apply_lever(state, lever):
  return [(state[i] + lever[i] - 1) % 3 + 1 for i in range(3)]

def search(target, limit):
  queue = [([], [3, 3, 3])]
  visited = []

  left = [1, 1, 0]
  right = [0, 1, 1]

  while queue:
    path, state = queue.pop(0)
    if state == target:
      return path
    if len(path) < limit:
      if state not in visited:
        visited.append(state)
        queue.append((path + ['left'], apply_lever(state, left)))
        queue.append((path + ['right'], apply_lever(state, right)))
  return None

if __name__ == "__main__":
  with open("input.txt") as f:
    for line in f:
      target, limit = get_instruction(line)
      result = search(target, limit)
      print(" ".join(result) if result else "Megoldhatatlan")
