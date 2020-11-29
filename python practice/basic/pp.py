fruits = ['apple', 'orange', 'grape']
fruits.insert(0, 'pine')
fruits.append('peach')
fruits.extend(['lemon', 'melon'])

boys = {
  'john': {
    'age': 20,
    'hobby': 'fishing',
    'job': 'hunter'
  },
  'mike': {
    'age': 21,
    'hobby': 'singing',
    'job': 'assasin'
  }
}

for index, value in enumerate(fruits):
  print(index, value)

for i in boys:
  for f in boys[i]:
    print(i, f, boys[i][f])