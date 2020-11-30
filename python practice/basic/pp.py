fruits = ['apple', 'orange', 'grape']
fruits.insert(0, 'pine')
fruits.append('peach')
fruits.extend(['lemon', 'melon'])

boys = {
  'john': {
    'age': 21,
    'hobby': 'fisihing'
  },
  'mike': {
    'age': 22,
    'hobby': 'singing'
  }
}

# for fruit in fruits:
#   print(fruit)

# for key1 in boys:
#   for key2 in boys[key1]:
#     print(key1, key2, boys[key1][key2])

import random as rand

# def make_array():
#   num = []
#   for i in range(1000):
#     num.append(rand.randint(1,100)
#   return num

# def array_count(x):
#   n = x.count(100)
#   print(n)

def make_rand():
  n = []
  for i in range(1000):
    n.append(rand.randint(1,10))
  return n

def array_count(x):
  print(x.count(10))

array_count(make_rand())
