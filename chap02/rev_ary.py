def ary_reverse(a):
  for i in range(len(a)//2):
    a[i], a[len(a)-i-1] = a[len(a)-i-1], a[i]


height = []
number = int(input("요소 개수: "))
print(f"{number}개의 정수를 입력하세요")
for i in range(number):
  height.append(int(input("x[%d] : "%i)))
  
ary_reverse(height)
print(f"배열의 요소를 역순으로 정렬했습니다.")
for i, element in enumerate(height):
  print(f"x[{i}] = {element}")  
