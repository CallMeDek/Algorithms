from abc import ABCMeta, abstractmethod

class Sort(metaclass=ABCMeta):
  def __init__(self):
    self._list = []
    self._size = 0

  @property
  def list(self):
    return self._list


  @property
  def size(self):
    return self._size


  def _set_size(self): 
    while(True):
      try:
        size = int(input("요소 개수: "))
        if size < 0:
          raise ValueError
      except ValueError:
        continue
      break
    self._size = size


  def get_values(self):
    self._set_size()
    size = self.size
    x = self.list
    for i in range(size):
      while(True):
        try:
          value = int(input(f"x[{i}]: "))
        except ValueError:
          continue
        break
      x.append(value)   


  def print_values(self):
    x = self.list
    for ele in x:
      print(f"{ele} ", end="")
    print()


  @abstractmethod
  def sort(self):
    pass


  @abstractmethod
  def recursive_sort(self, start, end):
    pass
