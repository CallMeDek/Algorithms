pos = []
flag_a = []
flag_b = []
flag_c = []

def Print(a):
  for ele in a:
    print(f"{ele} ", end="")
  print()


def Set(i):
  global pos;
  global flag_a;
  global flag_b;
  global flag_c;
  for j in range(8):
    if (not flag_a[j]) and (not flag_b[i + j]) and (not flag_c[i - j + 7]):
      pos[i] = j
      if i == 7:
        Print(pos)
      else:
        flag_a[j] = flag_b[i + j] = flag_c[i -j + 7] = 1
        Set(i + 1)
        flag_a[j] = flag_b[i + j] = flag_c[j -j + 7] = 0


for _ in range(8):
  pos.append(0)
  flag_a.append(0)

for _ in range(15):
  flag_b.append(0)
  flag_c.append(0)

Set(0)
