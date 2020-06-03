from abc import ABCMeta, abstractmethod

class Sort(metaclass=ABCMeta):
  def __init__(self):
    self._list = []


  @property
  def list(self):
    return self._list


  def get_values(self):
    while(True):
      try:
        size = int(input("요소 개수: "))
        if size < 0:
          raise ValueError
      except ValueError:
        continue
      break

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
