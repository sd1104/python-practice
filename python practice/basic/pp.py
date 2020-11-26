fruits = ['apple', 'orange', 'grape']
fruits.insert(0, 'pine')
fruits.append('peach')
fruits.extend(['lemon', 'melon'])

boys = {
  'john': {
    'age': 21,
    'hobby': 'fishing',
    'job': 'police'
  },
  'mike': {
    'age': 22,
    'hobby': 'singing',
    'job': 'diver'
  }
}

import random as ra

lucky = ra.randint(1,10)

if lucky == 10:
  print('lucky')
elif lucky == 4:
  print('unlucky')
else:
  print('normal')
