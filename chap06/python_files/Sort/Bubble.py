from abc import ABCMeta
from abc import abstractmethod

class Bubble(metaclass=ABCMeta):
  def __init__(self):
    self._a = []


  @property
  def a(self):
    return self._a

  
  def copy(self, x):
    for ele in x:
      self._a.append(ele)


  def print_sort(self):
    x = self._a
    for ele in x:
      print(f"{ele} ", end="")
    print()


  @abstractmethod
  def bubble_sort(self, x):
    pass


class Bubble1(Bubble):
  def __init__(self):
    super().__init__()
    

  def copy(self, x):
    super().copy(x)


  def bubble_sort(self):
    x = super().a
    for i in range(len(x)-1):
      for j in range(len(x)-1-i):
        if(x[j] > x[j + 1]):
          x[j], x[j + 1] = x[j + 1], x[j]


  def print_sort(self):
    print("Bubble1 : ")
    super().print_sort()


class Bubble2(Bubble):
  def __init__(self):
    super().__init__()
    

  def copy(self, x):
    super().copy(x)


  def bubble_sort(self):
    x = super().a
    for i in range(len(x)-1):
      exchange_counter = 0
      for j in range(len(x)-1-i):
        if(x[j] > x[j+1]):
          x[j], x[j+1] = x[j+1], x[j]
          exchange_counter += 1
      if exchange_counter != 0:
        break


  def print_sort(self):
    print("Bubble2 : ")
    super().print_sort()


class Bubble3(Bubble):
  def __init__(self):
    super().__init__()
    

  def copy(self, x):
    super().copy(x)


  def bubble_sort(self):
    x = super().a
    i = 0
    while(i < len(x)-1):
      last = len(x)-1;
      for j in range(len(x)-1, i, -1):
        if(x[j-1] > x[j]):
          x[j-1], x[j] = x[j], x[j-1]
          last = j
      i = last


  def print_sort(self):
    print("Bubble3 : ")
    super().print_sort()
