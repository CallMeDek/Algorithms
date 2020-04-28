def max3(a, b, c):
  max = a;
  if(b > max): max = b
  if(c > max): max = c
 
  return max


def main():
  print(f"max3({3}, {2}, {1}) = {max3(3, 2, 1)}")
  print(f"max3({3}, {2}, {2}) = {max3(3, 2, 2)}")
  print(f"max3({2}, {3}, {1}) = {max3(2, 3, 1)}")
  print(f"max3({2}, {2}, {1}) = {max3(2, 2, 1)}")
  print(f"max3({1}, {2}, {1}) = {max3(1, 2, 1)}")
  print(f"max3({1}, {2}, {3}) = {max3(1, 2, 3)}")


main()
