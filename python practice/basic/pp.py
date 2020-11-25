fruits = ['apple', 'orange', 'grape']
fruits.insert(1, 'melon')
fruits.insert(0, 'pine')
fruits.append('peach')
fruits.extend(['kwi', 'lemon'])

boys = {
  'john': {
    'age': 21,
    'hobby': 'fishing'
  },
  'mike': {
    'age': 22,
    'hobby': 'singing'
  }
}

# for index, value in enumerate(fruits):
#   print(index, '=', value)

# for key1 in boys:
#   for key2 in boys[key1]:
#     print(key1, key2, boys[key1][key2])

import random

# def plus():
#   for i in range(10):
#     numA = random.randint(1,10)
#     numB = random.randint(1,10)
#     formula_text = "{} + {}"
#     finished_text = formula_text.format(numA, numB)
#     print(finished_text)

# plus()


def bingo():
  bingo = random.randint(1,75)
  count = 1

  while bingo != 1:
    count += 1
    bingo = random.randint(1,75)

  return count

def ten():
  count_array = []

  for i in range(10):
    count_array.append(bingo())

  return(count_array)
