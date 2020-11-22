fruits = ['apple', 'orange', 'grape']
fruits.append('melon')
fruits.insert(0, 'peach')
fruits.insert(5, 'lemon')
del fruits[5]


boys = {
   'John': {
     'age': 20,
     'hobby': 'fishing',
     'dream': 'pilot'
   },
   'Mike': {
     'age': 21,
     'hobby': 'singing',
     'dream': 'driver'
   }
}


for index, value in enumerate(fruits):
  print(index, value)

for i in boys:
  for e in boys[i]:
    print(i, e, boys[i][e])
