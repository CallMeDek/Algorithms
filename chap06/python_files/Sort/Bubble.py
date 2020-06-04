from Sort.Sort_template import Sort


class Bubble1(Sort):
  def get_list_len(self):
    return super().size


  def sort(self):
    x = super().list
    size = super().size
    for i in range(size-1):
      for j in range(size-1-i):
        if(x[j] > x[j + 1]):
          x[j], x[j + 1] = x[j + 1], x[j]


  def recursive_sort(self, start, end):
    print("It is not implemented yet so it starts iterative sorting automatically.")
    self.sort()


class Bubble2(Sort):
  def get_list_len(self):
    return super().size

  def sort(self):    
    x = super().list
    size = super().size
    for i in range(size-1):
      exchange_counter = 0
      for j in range(size-1-i):
        if(x[j] > x[j+1]):
          x[j], x[j+1] = x[j+1], x[j]
          exchange_counter += 1
      if exchange_counter == 0:
        break


  def recursive_sort(self, start, end):
    print("It is not implemented yet so it starts iterative sorting automatically.")
    self.sort()


class Bubble3(Sort):
  def get_list_len(self):
    return super().size
  

  def sort(self):
    x = super().list
    size = super().size
    i = 0
    while(i < size-1):
      last = size-1;
      for j in range(size-1, i, -1):
        if(x[j-1] > x[j]):
          x[j-1], x[j] = x[j], x[j-1]
          last = j
      i = last


  def recursive_sort(self, start, end):
    print("It is not implemented yet so it starts iterative sorting automatically.")
    self.sort()
