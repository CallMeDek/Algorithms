def factorial(n):
  return n*factorial(n-1) if n > 0 else 1

while(True):
  try:
    x = int(input("음이 아닌 정수를 입력하세요. "))
    if (x < 0):
      raise ValueError
  except ValueError:
    continue
  break

print(f"{x}의 순차곱셈 값은 {factorial(x)}입니다")
