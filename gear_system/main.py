def get_instruction(line): #get the target and the step limit
  #format: [int, int, int] int
  try:
    target, limit = eval(line.strip()), 8
  except:
    try:
      parts = line.strip().split("]")
      target = eval(parts[0] + "]")
      limit = int(parts[1].strip())
    except:
      return None, None
  return target, limit

def apply_lever(state, lever):
  return [(state[i] + lever[i] - 1) % 3 + 1 for i in range(3)]

#brute focing by creating all possible variations
def search(target, limit):
  queue = [([], [3, 3, 3])]
  tested = []

  left,right = [1, 1, 0], [0, 1, 1]

  while queue: #while there are remaining possibilities
    path, state = queue.pop(0) #get and remove first possibility
    if state == target:
      return path
    if len(path) < limit: #re-configure, combinatory
      if state not in tested:
        tested.append(state)
        #extend possibilities
        queue.append((path + ['left'], apply_lever(state, left)))
        queue.append((path + ['right'], apply_lever(state, right)))
  return None

if __name__ == "__main__": #ha egyensen ezt a fájlt inditjuk el (nem indul el ha esetleg imoprtálva van)
  with open("input.txt") as f:
    for line in f:
      target, limit = get_instruction(line)
      result = [] if not target or not limit else search(target, limit)
      print(" ".join(result) if result else "Megoldhatatlan")
