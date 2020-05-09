a = []
for i in range(5):
  a.append(int(input("a[%d] : " %(i))))

print("각 요소의 값");
for i in range(len(a)):
  print(f"a[{i}] = {a[i]}")
