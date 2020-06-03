from Sort.Sort_template import Sort

class Shell(Sort):
  def __init__(self):
    super().__init__()


  def get_values(self):
    super().get_values()

   
  def print_values(self):
    super().print_values() 
  

  def sort(self):
    x = super().list
    h = int(len(x) // 2)
    while(h > 0):
      for i in range(h, len(x)):
        j = i - h
        temp = x[i]
        while(j >= 0 and x[j] > temp):
          x[j + h] = x[j]
          j -= h
        x[j + h] = temp 
      h = int(h/2)


class Shell2(Sort):
  def __init__(self):
    super().__init__()


  def get_values(self):
    super().get_values()

   
  def print_values(self):
    super().print_values() 
  

  def sort(self):
    x = super().list
    h = 1
    while(h < len(x)/9):
      h = 3*h + 1

    while(h > 0):
      for i in range(h, len(x)):
        j = i - h
        temp = x[i]
        while(j >= 0 and x[j] > temp):
          x[j + h] = x[j]
          j -= h
        x[j + h] = temp 
      h = int(h/2)
