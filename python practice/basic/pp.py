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

# for index, value in enumerate(fruits):
#   print(index, '=', value)

# for key1 in boys:
#   for key2 in boys[key1]:
#     print(key1, key2, boys[key1][key2])