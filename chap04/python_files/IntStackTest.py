from Stack.int_stack import IntStack

def main():
  stack = IntStack(64)
  
  while(True):
    print(f"\n현재 데이터 수: {stack.Size()} / {stack.Capacity()}")
    while(True):
      try:
        menu = int(input("(1)Push (2)Pop (3)Peek (4)Print (5)Search (0)Terminate : "))
        if menu not in [0, 1, 2, 3, 4, 5]:
          raise ValueError
      except ValueError:
        continue
      break
    
    if menu == 0:
      break
    elif menu == 1:
      while(True):
        try:
          x = int(input("데이터 : "))
          if x < 0:
            raise ValueError
        except ValueError:
          continue
        break
      if(stack.Push(x) == -1):
        print("Error: Failed to push")
    elif menu == 2:
      x = stack.Pop()
      if(x == -1):
        print("Error: Failed to pop")
      else:
        print(f"Popped data: {x}")
    elif menu == 3:
      x = stack.Peek()
      if(x == -1):
        print("Error: Failed to peek")
      else:
        print(f"Peek data: {x}")
    elif menu == 4:
      stack.Print()
    else: 
      while(True):
        try:
          x = int(input("검색 데이터 : "))
          if x < 0:
            raise ValueError
        except ValueError:
          continue
        break
      idx = stack.Search(x)
      print(f"{x}: No such data.") if idx == -1 else print(f"{x} is the {idx}th elements from Top")

  stack.Terminate()

main()
