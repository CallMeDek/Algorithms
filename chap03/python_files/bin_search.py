def bin_search(a, pl, pr, key):
  if pl >= pr:
    if a[pl] == key:
      return pl
    else:
      return -1
  else:
    pc = (pl + pr)//2
    if a[pc] == key:
      return pc
    elif key < a[pc]:
      return bin_search(a, pl, pc - 1, key)
    else:
      return bin_search(a, pc + 1, pr, key)

print("이진 검색")
while(True):
  try:
    nx = int(input("요소 개수: ")) 
    if nx < 0:
      raise ValueError
  except ValueError:
    continue
  break

x = []
while(True):
  try:
    value = int(input("x[0]: "))
    x.append(value) 
  except ValueError:
    continue
  break

for i in range(1, nx):
  while(True):
    try:
      value = int(input(f"x[{i}]: "))
      if value < x[i-1]:
        raise ValueError
    except ValueError:
      continue
    x.append(value)
    break

while(True):
  try:
    key = int(input("검색값: ")) 
  except ValueError:
    continue
  break
    
idx = bin_search(x, 0, len(x)-1, key)
print("검색에 실패했습니다.") if idx == -1 else print(f"{key}는(은) x[{idx}]에 있습니다.")
