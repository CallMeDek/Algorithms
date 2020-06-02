from Sort.Bubble import Bubble1, Bubble2, Bubble3

while(True):
  try:
    print(f"버블 정렬")
    nx = int(input("요소 개수 : "))
    if nx < 0:
      raise ValueError
  except ValueError:
    continue
  break

x = []
for i in range(nx):
  while(True):
    try:
      n = int(input(f"x[{i}] : "))
      x.append(n)
    except ValueError:
      continue
    break

bubble = Bubble1()
bubble.copy(x)
bubble.bubble_sort()
bubble.print_sort() 

bubble = Bubble2()
bubble.copy(x)
bubble.bubble_sort()
bubble.print_sort() 

bubble = Bubble3()
bubble.copy(x)
bubble.bubble_sort()
bubble.print_sort() 
