def med3(a, b, c):
  if(a >= b):
    if(b >= c):
      return b;
    elif(a <= c):
      return a;
    else:
      return c;
  elif(a > c):
    return a;
  elif(b > c):
    return c;
  else:
    return b;


def main():
  print("Get a median among the three integers", end="\n");
  a = int(input("a : "))
  b = int(input("b : "))
  c = int(input("c : "))
  print(f"The median is {med3(a, b, c)}.", end="\n");

main()
