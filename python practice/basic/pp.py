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

for i in fruits:
  print(i)
