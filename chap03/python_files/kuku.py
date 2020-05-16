def sum_(a, b):
  return a + b


def mul_(a, b):
  return a * b


def kuku(func):
  for i in range(1, 10):
    for j in range(1, 10):
      print("%3d"% func(i, j), end="")
    print()


print("덧셈포")
kuku(sum_)
print("곱셈표")
kuku(mul_)
