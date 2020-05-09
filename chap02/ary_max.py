def maxof(a):
  max_ = a[0]
  for element in a:
    if(element > max_): max_ = element
  return max_

height = []
number = int(input("사람 수: "))
print(f"{number} 사람의 키를 입력하세요.")
for i in range(number):
  height.append(int(input("height[%d] : " % i)))

print(f"최댓값은 {maxof(height)}입니다.")
