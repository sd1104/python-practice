fruits = ['apple', 'orange', 'grape']
fruits.insert(0, 'pine')
fruits.append('peach')
fruits.extend(['lemon', 'melon'])

boys = {
  'john': {
    'age': 21,
    'hobby': 'fising'
  },
  'mike': {
    'age': 22,
    'hobby': 'singing'
  }
}

import random as rand


def omikuzi():
  lucky = 0
  unlucky= 0
  normal = 0
  for i in range(1000):
    num = rand.randint(1,10)
    if num == 10:
      lucky += 1
    elif num == 5:
      unlucky += 1
    else:
      normal += 1
  print(lucky, unlucky, normal)

omikuzi()