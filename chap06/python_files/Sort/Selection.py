class Selection:
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


  def selection_sort(self):
    x = self.a
    for i in range(len(x)):
      min_index = i
      for j in range(i+1, len(x)):
        if x[j] < x[min_index]:
          min_index = j
      x[i], x[min_index] = x[min_index], x[i]
