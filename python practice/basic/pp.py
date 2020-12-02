fruits = ['apple', 'orange', 'grape']
fruits.insert(0, 'pine')
fruits.append('lemon')

jump = [121, -1, 12.1, 1000, 125, 126, 128, 129, 130, 150, 0, 'F', 150, 156, 80, 500, -6, 122.55]
max = 150

def count(jump, max):
  digit = 0
  abnormal = 0
  illegal = 0

  for i in range(len(jump)):
    if type(jump[i]) == float:
      digit += 1

  max = max
  for i in range(len(jump)):
    if type(jump[i]) == str:
      continue
    elif jump[i] > max or jump[i] < 0:
      abnormal += 1

  for i in range(len(jump)):
    if type(jump[i]) == str:
      illegal += 1
    elif jump[i] == 0:
      illegal += 1

  error = digit + abnormal + illegal

  return digit, abnormal, illegal, error

print(count(jump, max))