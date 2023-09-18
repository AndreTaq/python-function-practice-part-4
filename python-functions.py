# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
  return max([a, b, c])

print(max_num(1, 7, 4))
print(max_num(40, 20, 60))
print(max_num(500, 200, 300))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(lst):
  if len(lst) == 0:
    return 0
    
  items = lst[0]

  if len(lst) > 1:
    for i in lst[1:]:
      items = items * i

  return items

print(mult_list([5,6,]))
print(mult_list([]))

# Write a Python function called rev_string() to reverse a string.
def rev_string(string):
  return string[::-1]

print(rev_string("123456"))
print(rev_string("Hello World"))

# Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(a,b,c):
  return a in range(b,c+1)

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      length = len(row_prev)+1
      for i in range(length):
        if i == 0:
          row.append(1)
          
        elif i > 0 and i < length-1:
          row.append(triangle[row_number - 1][i-1]+triangle[row_number - 1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    for row in triangle:
      print(row)

pascal(2)
pascal(5)