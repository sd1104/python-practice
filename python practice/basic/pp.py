fruits = ['apple', 'orange', 'grape']

fruits.append('lemon')
fruits.insert(0, 'pine')
fruits.extend(['strawberry', 'melon'])

boys = {
  'john': {
    'age': 20,
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

import random as rand

num = rand.randint(1,10)

if num == 10:
  print('lucky')
elif num == 4:
  print('unlucky')
else:
  print('See you next!')
