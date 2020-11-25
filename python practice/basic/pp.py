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

for index, value in enumerate(fruits):
  print(index, '=', value)
