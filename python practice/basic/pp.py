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

num = 0
i = 0
while i<10:
  num += i+1
  i+=1
print(num)
