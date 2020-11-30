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

for fruit in fruits:
  print(fruit)