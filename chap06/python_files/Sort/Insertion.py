class Insertion:
  def __init__(self):
    self._a = [] 


  @property
  def a(self):
    return self._a


  def get_values(self):
    while(True):
      try: 
        nx = int(input("요소 개수: "))
        if nx < 0:
          raise ValueError
      except ValueError:
        continue
      break

    for i in range(nx):
      x = self.a
      while(True):
        try:
          val = int(input(f"x[{i}] : "))
        except ValueError:
          continue
        break
      x.append(val)


  def print_values(self):
    x = self.a
    for ele in x:
      print(f"{ele} ", end="")
    print()


  def insertion_sort(self):
    x = self.a
    for i in range(1, len(x)):
      tmp = x[i]
      j = i
      while(j > 0 and x[j-1] > tmp):
        x[j] = x[j-1]
        j -= 1
      x[j] = tmp
        
