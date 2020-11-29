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

for fruit in fruits:
  print(fruit)

for key1 in boys:
  for key2 in boys[key1]:
    print(key1, key2, boys[key1][key2])

num = 0
for i in range(10):
  num += i+1
print(num)