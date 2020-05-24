class IntQueue:
  def __init__(self, max_):
      self._maximum = max_
      self._num = 0
      self._front = 0
      self._rear = 0
      self._que = []
      self._init_que()      


  @property
  def maximum(self):
    return self._maximum


  @property
  def num(self):
    return self._num if self._num >= 0 else -1

  
  @property
  def front(self):
    return self._front if 0 <= self._front < self._maximum else -1


  @property 
  def rear(self):
    return self._rear if 0 <= self._rear < self._maximum else -1

   
  @maximum.setter
  def maximum(self, max_):
    try:
      if isinstance(max_, int):
        if 0 <= max_:
          self._maximum = max_
        else:
          raise ValueError
      else:
        raise TypeError
    except TypeError:
      print(f"MAX: {_max} is not an integer")
      sys.exit(1)
    except ValueError:
      print(f"MAX: {_max} is not valid")
      sys.exit(1)


  @num.setter
  def num(self, num):
    try:
      if isinstance(num, int):
        if 0 <= num < self._maximum:
          self._num = num
        else:
          raise ValueError
      else:
        raise TypeError
    except TypeError:
      print(f"NUM: {num} is not an integer")
      sys.exit(1)
    except ValueError:
      print(f"NUM: {num} is not valid")
      sys.exit(1)


  @front.setter
  def front(self, front):
    try:
      if isinstance(front, int):
        if 0 <= front < self._maximum:
          self._front = front
        else:
          raise ValueError
      else:
        raise TypeError
    except TypeError:
      print(f"FRONT: {front} is not an integer")
      sys.exit(1)
    except ValueError: 
      print(f"FRONT: {front} is not valid")
      sys.exit(1)    


  @rear.setter
  def rear(self, rear):
    try:
      if isinstance(rear, int):
        if 0 <= rear < self._maximum:
          self._rear = rear
        else:
          raise ValueError
      else:
        raise TypeError
    except TypeError:
      print(f"REAR: {rear} is not an integer")
      sys.exit(1)
    except ValueError:
      print(f"REAR: {rear} is not an integer")
      sys.exit(1)


  def _init_que(self):
    for _ in range(self._maximum):
      self._que.append(-1)
 

  def Enque(self, x):
    try:
      if isinstance(x, int):
        if self._IsFull():
          return -1
        else:
          self._num += 1
          self._que[self._rear] = x
          self._rear = (self._rear + 1) % self._maximum
      else:
        raise TypeError
    except TypeError:
      print(f"ENQUE: {x} is not valid")
      sys.exit(1)


  def Deque(self):
    if self._IsEmpty():
      return -1
    else:
      self._num -= 1
      x = self._que[self._front]
      self._front = (self._front + 1) % self._maximum
      return x
      

  def Peek(self):
    if self._IsEmpty():
      return -1
    else:
      return self._que[self._front]


  def Clear(self):
    self._num = 0
    self._front = 0
    self._rear = 0


  def Capcity(self):
    return self._maximum


  def Size(self):
    return self._num


  def _IsEmpty(self):
    return self._num <= 0


  def _IsFull(self):
    return self._num >= self._maximum


  def Search(self, x): 
    try:
      if isinstance(x, int):
        for i in range(self._num):
          idx = (i + self._front) % self._maximum
          if(self._que[idx] == x):
            return idx
        return -1
      else:
        raise TypeError
    except TypeError:
      print(f"SEARCH: {x} is not valid")
      sys.exit(1)


  def Print(self):
    for i in range(self._num):
      print(f"{self._que[(i + self._front) % self._maximum]} ", end="")
    print()


  def Terminate(self):
    del self._que
    self._maximum = 0
    self._num = 0
    self._front = 0
    self._rear = 0

