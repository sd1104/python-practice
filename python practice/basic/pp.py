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

num = 0
i = 0
while i < 10:
  num = (i+1) + (i+2)
  i += 1
print(num)
