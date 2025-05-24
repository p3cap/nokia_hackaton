## fibonacci numbers divideable by 3
def fibonacci_div_3(n:int):
  #validating
  if n.isnumeric(): n = int(n)
  else: return []

  num, upcoming = 0, 1 #first and next possible sulution
  result = []
  while num <= n:
    if num % 3 == 0:
      result.append(num)
    num, upcoming = upcoming, num + upcoming #fibonacci sequence: "each number is equal to the sum of the preceding two numbers"
    
  return result

if __name__ == "__main__": #ha egyensen ezt a fájlt inditjuk el (nem indul el ha esetleg imoprtálva van)
  with open('./input.txt', 'r') as f:
    input = f.read()

  for line in input.strip().splitlines():
    result = [str(item) for item in fibonacci_div_3(line)] #stringify
    print(', '.join(result) if result else "N/A")

