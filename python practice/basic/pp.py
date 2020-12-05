

def excel_array():
  ary = ''
  for i in range(10):
    text = 'C' + str(i+1) + ',' + ' '
    ary = ary + text
  return ary

print(excel_array())
