from random import randint

def maxof(a):
  max = a[0]
  for element in a:
    if(element > max): max = element
  return max


height = []
number = int(input("사람 수: "))
print(f"{number}사람의 키를 입력하세요.")
for i in range(number):
  height.append(100 + randint(0, 90))
  print(f"height[{i}] = {height[i]}")
print(f"최대값은 {maxof(height)}입니다.")
