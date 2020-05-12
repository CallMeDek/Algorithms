def search(a, key):
  i = 0
  while(True):
    if(a[i] == key):
      break
    i += 1
  return -1 if i == len(a)-1 else i

print("선형 검색(보초법)");
while(1):
  try:
    nx = int(input("요소 개수: "))
    if nx < 0:
      raise ValueError
  except ValueError:
    continue
  break

x = []
for i in range(nx+1):
  x.append(int(input(f"x[{i}] : ")))

while(1):
  try:
    key = int(input("검색값: "))
  except ValueError:
    continue
  break

idx = search(x, key)
if(idx == -1):
  print("검색에 실패했습니다.")
else:
  print(f"{key}(은)는 x[{idx}]에 있습니다.")
