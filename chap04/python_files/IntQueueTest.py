from Queue.int_queue import IntQueue

que = IntQueue(64)

while(True):
  print(f"현재 데이터 수: {que.Size()} / {que.Capcity()}")
  while(True):
    try:
      m = int(input("(1)인큐 (2)디큐 (3)피크 (4)출력 (0)종료: "))
      if m not in [0, 1, 2, 3, 4]:
        raise ValueError
    except ValueError:
      continue
    break
  
  if m == 0:
    break
  elif m == 1:
    while(True):
      try:
        x = int(input("데이터: "))
        if x < 0:
          raise ValueError
      except ValueError:
        continue
      break
    if(que.Enque(x) == -1):
      print("인큐에 실패했습니다.")
  elif m == 2:
    x = que.Deque()
    if(x == -1):
      print("디큐에 실패했습니다.")
    else:
      print(f"디큐한 데이터는 {x}입니다.")
  elif m == 3:
    x = que.Peek()
    if(x == -1):
      print("피크에 실패했습니다")
    else:
      print(f"피크한 데이터는 {x}입니다.")
  else:
    que.Print()
  print()

que.Terminate()
