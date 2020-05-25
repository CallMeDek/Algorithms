def gcd(x, y):
  return x if y == 0 else gcd(y, x % y)


def get_integer():
  while(True):
    try:
      x = int(input("정수를 입력하세요: "))
      if x < 0:
        raise ValueError
    except ValueError:
      continue
    break
  return x

x = get_integer()
y = get_integer()
print(f"최대공약수는 {gcd(x, y)}입니다.")
