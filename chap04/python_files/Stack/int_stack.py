class IntStack:
  def __init__(self, max_):
    self._ptr = 0
    self._stk = []
    try:
      self._max = int(max_)
    except ValueError:
      print("MAX value is not avaliable")
      sys.exit(1)
    for i in range(self._max):
      self._stk.append(-1)  
 

  def _IsEmpty(self):
    return self._ptr <= 0

  
  def _IsFull(self):
    return self._ptr >= self._max 


  def Capacity(self):
    return self._max


  def Size(self):
    return self._ptr


  def Search(self, x):
    if isinstance(x, int) is False:
      return -1
    for i in range(self._ptr-1, -1, -1):
      if(self._stk[i] == x):
        return i
    return -1


  def Print(self):
    for i in range(self._ptr):
      print(f"{self._stk[i]} ", end=" ");
    print()


  def Terminate(self):
    del self._stk
    self._ptr = self._max = 0


  def Push(self, x):
     if isinstance(x, int) is False:
       return -1
     if self._IsFull():
       return -1
     self._stk[self._ptr] = x
     self._ptr += 1


  def Pop(self):
    if self._IsEmpty():
      return -1
    x = self._stk[self._ptr-1]
    self._ptr -= 1
    return x


  def Peek(self):
    if self._IsEmpty():
      return -1
    return self._stk[self._ptr-1]


  def Clear(self):
    self._ptr = 0

  
