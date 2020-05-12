def search(a, key):
  i = 0
  while(True):
    if(i == len(a)):
      return -1
    if(a[i] == key):
      return i
    i += 1

print("선형검색")
while(True):
  try:
    nx = int(input("요소 개수: "))
    if nx < 0:
      raise ValueError
  except ValueError:
    continue
  break

x = []
for i in range(nx):
   x.append(int(input("x[%d] : "%i)))
while(True):
  try:
    key = int(input("검색값 : "));
  except ValueError:
    continue
  break
idx = search(x, key)
alarm = f"{key}(은)는 x[{idx}]에 있습니다." if idx != -1 else "검색에 실패했습니다."
print(alarm)
