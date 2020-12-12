
fruits = ['apple', 'orange', 'grape']

# print(fruits)

boys = {
  'john': {
    'age': 21,
    'hobby': 'fishing'
  },
  'mike': {
    'age': 21,
    'hobby': 'singing'
  }
}

# for fruit in fruits:
#   print(fruit)

# for key1 in boys:
#   for key2 in boys[key1]:
#     print(key1, key2, boys[key1][key2])

# num = 0
# for i in range(10):
#   num = (i+2) + (i+1)
# print(num)

import random as rand

numA = rand.randint(1,5)

if numA == 5:
  print('lucky')
elif numA == 4:
  print('unlucky')
else:
  print('tyuukichi')