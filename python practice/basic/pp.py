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

def make_plus():
  i = 0
  while i < 10:
    numA = random.randint(0,10)
    numB = random.randint(0,10)
    plus = numA + numB
    formula = '{} + {}'
    formula1 = formula.format(numA, numB)
    print(formula1)
    i += 1

height = 101

if height == 180:
  print(180)
elif height == 100:
  print(100)
else:
  print('other')